class Party:
    def __init__(self, party_name, party_votes):
        self.name = party_name
        self.votes = party_votes
        self.eligible = None

    def is_eligible(self, threshold, total_votes):
        self.eligible = self.votes / total_votes > threshold
        return self.eligible
