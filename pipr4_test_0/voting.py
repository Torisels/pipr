
from collections import Counter


class Voting:

    def __init__(self, tickets, parties: {}, threshold):
        self.total_votes = sum([votes for votes in parties.values()])
        self.tickets = tickets
        self.threshold = threshold
        self.eligible_parties, self.not_eligible_parties = self.filter_parties(parties)
        self.quotients = self.get_quotients()
        self.tickets_counter = self.get_tickets()

    def filter_parties(self, parties):
        eligible = list()
        not_eligible = list()

        for party, votes in parties.items():
            if self.party_is_eligible(votes):
                eligible.append((party, votes))
            else:
                not_eligible.append(party)
        return eligible, not_eligible

    def get_quotients(self):
        quotients = list()
        for party, votes in self.eligible_parties:
            for q in range(1, 2 * self.tickets + 2, 2):
                quotients.append((party, votes / q))
        return sorted(quotients, key=lambda x: x[1], reverse=True)

    def get_tickets(self):
        tickets_counter = Counter()
        for party, quotient in self.quotients[:self.tickets]:
            tickets_counter[party] += 1
        return tickets_counter

    def party_is_eligible(self, votes):
        return votes / self.total_votes > self.threshold

    def print_results(self):
        print("Parties which had more than 5% of votes: ")
        for party, tickets in self.tickets_counter.items():
            print(f"{party} have {tickets} tickets.")
        print("\nParties below threshold: ")
        for party in self.not_eligible_parties:
            print(f"{party} have 0 tickets.")
