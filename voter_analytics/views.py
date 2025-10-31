# File: voter_analytics/views.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 10/31/2025
# Description: Defines the views (including class-based views) for handling voter data and displaying the results.
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from . models import *
from datetime import date
import plotly
import plotly.graph_objs as go

# Create your views here.

class VoterListView(ListView):
    '''View to display voter results'''

    template_name = "voter_analytics/voters.html"
    model = Voter
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        """filters qs"""

        voters = Voter.objects.all()

        # party aff
        party_affiliation = self.request.GET.get('party_affiliation')
        if party_affiliation:
            voters = voters.filter(party_affiliation__iexact=party_affiliation)
            print(self.request.GET)

        # min birth year
        min_birth_year = self.request.GET.get('min_birth_year')
        if min_birth_year:
            min_birth_date = date(int(min_birth_year), 1, 1)
            voters = voters.filter(dob__gte=min_birth_date)

        # max birth year
        max_birth_year = self.request.GET.get('max_birth_year')
        if max_birth_year:
            max_birth_date = date(int(max_birth_year), 12, 31)
            voters = voters.filter(dob__lte=max_birth_date)

        # voter score
        voter_score = self.request.GET.get('voter_score')
        if voter_score:
            voters = voters.filter(voter_score=voter_score)

        # voted elections
        for field in ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']:
            if self.request.GET.get(field):
                voters = voters.filter(**{field: True})

        return voters

    def get_context_data(self, **kwargs):
        """
        provides context to template
        """

        context = super().get_context_data(**kwargs)
        current_year = date.today().year
        context['all_years'] = list(range(current_year, 1919, -1))
        context['scores'] = range(0, 6)
        context['party_affiliation'] = self.request.GET.get('party_affiliation')
        context['min_birth_year'] = self.request.GET.get('min_birth_year')
        context['max_birth_year'] = self.request.GET.get('max_birth_year')
        context['voter_score'] = self.request.GET.get('voter_score')
        context['v20state'] = self.request.GET.get('v20state')
        context['v21town'] = self.request.GET.get('v21town')
        context['v21primary'] = self.request.GET.get('v21primary')
        context['v22general'] = self.request.GET.get('v22general')
        context['v23town'] = self.request.GET.get('v23town')
        context['action'] = 'voters_list'

        return context

class VoterDetailView(DetailView):
    """
    view for single voter
    """

    model = Voter
    template_name = "voter_analytics/single_voter.html"
    context_object_name = "voter"

    def get_context_data(self, **kwargs):
        """
        provides context to template
        """

        context = super().get_context_data(**kwargs)
        voter = context['voter']
        address = f"{voter.street_number} {voter.street_name}, Boston, MA {voter.zip_code}"
        google_maps = f"https://www.google.com/maps/search/{address.replace(' ', '+')}"
        context['link'] = google_maps

        return context

class VoterGraphsView(ListView):
    """
    view for graphs representing voting data
    """

    template_name = 'voter_analytics/graphs.html'
    model = Voter
    context_object_name = 'voter'

    def get_queryset(self):
        """filters qs"""

        voters = Voter.objects.all()

        # party aff
        party_affiliation = self.request.GET.get('party_affiliation')
        if party_affiliation:
            voters = voters.filter(party_affiliation__iexact=party_affiliation)
            print(self.request.GET)

        # min birth year
        min_birth_year = self.request.GET.get('min_birth_year')
        if min_birth_year:
            min_birth_date = date(int(min_birth_year), 1, 1)
            voters = voters.filter(dob__gte=min_birth_date)

        # max birth year
        max_birth_year = self.request.GET.get('max_birth_year')
        if max_birth_year:
            max_birth_date = date(int(max_birth_year), 12, 31)
            voters = voters.filter(dob__lte=max_birth_date)

        # voter score
        voter_score = self.request.GET.get('voter_score')
        if voter_score:
            voters = voters.filter(voter_score=voter_score)

        # voted elections
        for field in ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']:
            if self.request.GET.get(field):
                voters = voters.filter(**{field: True})

        return voters

    def get_context_data(self, **kwargs):
        """
        provides context to template
        """

        context = super().get_context_data(**kwargs)
        filtered = self.get_queryset()

        # histogram
        dob_year = [voter.dob.year for voter in filtered]
        fig_one = go.Histogram(x=dob_year, nbinsx=100)
        title_one = f"Voter Distribution by Birth Year (n={len(dob_year)})"

        layout_one = go.Layout(
            bargap=0.5,
            xaxis=dict(title='Birth Year'),
            yaxis=dict(title='Count')
        )

        graph_div_birth = plotly.offline.plot({"data": [fig_one],
                                               "layout": layout_one,
                                               "layout_title_text": title_one,},
                                              auto_open=False,
                                              output_type="div")

        # pie
        party_count = {}
        for voter in filtered:
            party_aff = voter.party_affiliation
            party_count[party_aff] = party_count.get(party_aff, 0) + 1
        fig_two = go.Pie(labels=list(party_count.keys()), values=list(party_count.values()))
        title_two = f"Voter Distribution by Party (n={len(filtered)})"
        graph_div_party = plotly.offline.plot({"data": [fig_two],
                                               "layout_title_text": title_two,},
                                                auto_open=False,
                                                output_type="div")

        # bar
        elections = ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']
        vote_count = []
        for election in elections:
            count = filtered.filter(**{election: True}).count()
            vote_count.append(count)
        fig_three = go.Bar(x=elections, y=vote_count)
        title_three = f"Vote Count by Voted Elections (n={Voter.objects.count()})"
        graph_div_elections = plotly.offline.plot({"data": [fig_three],
                                                   "layout_title_text": title_three,},
                                                    auto_open=False,
                                                    output_type="div")

        # graphs
        context['graph_div_birth'] = graph_div_birth
        context['graph_div_party'] = graph_div_party
        context['graph_div_elections'] = graph_div_elections
        # old context
        current_year = date.today().year
        context['all_years'] = list(range(current_year, 1919, -1))
        context['scores'] = range(0, 6)

        context['party_affiliation'] = self.request.GET.get('party_affiliation')
        context['min_birth_year'] = self.request.GET.get('min_birth_year')
        context['max_birth_year'] = self.request.GET.get('max_birth_year')
        context['voter_score'] = self.request.GET.get('voter_score')
        context['action'] = 'voter_graphs'

        return context