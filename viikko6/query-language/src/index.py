from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, \
        Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
    
    for player in stats.matches(matcher):
        print(player)

    print("-------------------------------")

    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )
    
    for player in stats.matches(matcher):
        print(player)

    print("-------------------------------")

    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )
    
    for player in stats.matches(matcher):
        print(player)

    print("-------------------------------")
    
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    print("-------------------------------")
    
    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    for player in stats.matches(matcher):
        print(player)

    print("-------------------------------")
    
    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )


    for player in stats.matches(matcher):
        print(player)

    print("-------------------------------")
    
    query = QueryBuilder()
    matcher = query.playsIn("NYR").hasAtLeast(10, "goals").hasFewerThan(20, "goals").build()
    
    for player in stats.matches(matcher):
        print(player)


    print("-------------------------------")
    
    query = QueryBuilder()
    matcher = (
        query
            .oneOf(
                query.playsIn("PHI")
                    .hasAtLeast(10, "assists")
                    .hasFewerThan(5, "goals")
                    .build(),
                query.playsIn("EDM")
                    .hasAtLeast(50, "points")
                    .build()
            )
            .build()
        )

    
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
