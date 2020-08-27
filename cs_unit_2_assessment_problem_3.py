def uncover_spy(n, trust):
    """
    Finds the spy (trusted by all citizens, but trusts nobody) in the population.
    """
    # trust_graph = {}
    # Note: Graph would be more efficient, but out of time! So just adding MVP below.

    trusters = [trust_link[0] for trust_link in trust]
    trusted = [trust_link[1] for trust_link in trust]

    for person_num in range(n):
        person = person_num + 1
        trusts = 0
        trusted_by = 0
        # Find out how many people this person trusts, and how many he/she/they is trusted by:
        if person in trusters:
            trusts = sum([p == person for p in trusters])
        if person in trusted:
            trusted_by = sum([p == person for p in trusted])
        # If this person trustss nobody but is trusted by everyone, he/she/they is the spy!:
        if trusts == 0 and trusted_by == n - 1:
            return person

    # If no spies that meet the above criteria, then return -1 to indicate there is no spy 
    # in the population:
    return -1

if __name__ == "__main__":
    # n = 4
    # trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]
    spy = uncover_spy(n=4, trust=[[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]])
    print(spy)
