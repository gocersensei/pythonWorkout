import operator

PEOPLE = [('Joe', 'Biden', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]


def format_sort_records(list_of_tuples):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list_of_tuples,
                         key=operator.itemgetter(1, 0)):
        # You can use operator.itemgetter with any data structure that
        # takes square brackets. You can also pass it more than one
        # argument, as seen here.
        output.append(template.format(*person))
        return output


print('\n'.join(format_sort_records(PEOPLE)))
