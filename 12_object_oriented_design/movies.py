"""
Exercise 12.1.11

Discovering Computer Science, Second Edition
Jessen Havill
"""

class Movie:
    # fill this in

def readMovies(filename):
    """Create a list of Movie objects from a file."""
    
    castFile = open(filename, 'r', encoding = 'utf-8')
    movies = []
    for line in castFile:
        line = line.strip()
        items = line.split('\t')
        movie = items[0][:-7]
        year = items[0][-5:-1]
        actors = items[1:]
        movie = Movie(movie, int(year), actors)
        movies.append(movie)
    castFile.close()
    return movies
    
def search(movies, title):
    """Search for a movie title in a list of movies."""
    
    for movie in movies:
        if movie.getTitle() == title:
            return movie
    return None

def main():
    movies = readMovies('movies2013.txt')
    title = input('Movie title (or q to quit): ')
    while title not in 'qQ':
        movie = search(movies, title)
        if movie == None:
            print('That movie was not found.')
        else:
            print('\n' + movie.getTitle() + ' (' + str(movie.getYear()) + ')')
            response = input('(P)rint actors, (A)dd actor, or show (C)ommon actors? ')
            if response in 'aA':
                name = input('Actor name: ')
                movie.addActor(name)
            elif response in 'cC':
                otherTitle = input('Movie title: ')
                otherMovie = search(movies, otherTitle)
                if otherMovie == None:
                    print('That movie was not found.')
                else:
                    if movie.commonActors(otherMovie):
                        print('Yes, "' + movie.getTitle() + '" and "' + otherTitle + '" have common actors.')
                    else:
                        print('No, "' + movie.getTitle() + '" and "' + otherTitle + '" do not have common actors.')
            elif response in 'pP':
                for actor in movie.getActors():
                    print('    ' + actor)
        title = input('\nMovie title (or q to quit): ')

main()