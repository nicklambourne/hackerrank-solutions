from operator import itemgetter


def person_lister(f):
    def inner(people):
        for i in people:
            i[2] = int(i[2])
        persons = sorted(people, key=itemgetter(2))
        for i in range(len(persons)):
            persons[i] = f(persons[i])
        return persons
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')