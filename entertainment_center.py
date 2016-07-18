import media
import fresh_tomatoes

# Credit: movie storylines were taken from http://www.imdb.com

# Movie instance 1
sandlot = media.Movie("The Sandlot",
                      "A new kid in town is taken under the wing of a young \
                      baseball prodigy and his team in this coming of age \
                      movie set in the summer of 1962.",
                      "1993",
                      "https://upload.wikimedia.org/wikipedia/en/d/d4/Sandlot_poster.jpg",  # noqa
                      "https://youtu.be/-QDq-e1GbjE")
# Movie instance 2
mrs_doubtfire = media.Movie("Mrs. Doubtfire",
                            "After a bitter divorce, an actor disguises \
                            himself as a female housekeeper to spend time \
                            with his children held in custody by his former \
                            wife.",
                            "1993",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Mrs_Doubtfire.jpg/220px-Mrs_Doubtfire.jpg",  # noqa
                            "https://youtu.be/PqxpC_jYncE")
# Movie instance 3
wedding_crashers = media.Movie("Wedding Crashers",
                              "John Beckwith and Jeremy Grey, a pair of \
                              committed womanizers who sneak into weddings \
                              to take advantage of the romantic tinge in the \
                              air, find themselves at odds with one another \
                              when John meets and falls for Claire Cleary.",
                              "2005",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Wedding_crashers_poster.jpg/215px-Wedding_crashers_poster.jpg",  # noqa
                              "https://youtu.be/VYrEQbtV2V4")
# Movie instance 4
days_of_thunder = media.Movie("Days of Thunder",
                              "A young hot-shot stock car driver gets his \
                              chance to compete at the top level.",
                              "1990",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/d/d8/Days_of_thunder.jpg/220px-Days_of_thunder.jpg",  # noqa
                              "https://youtu.be/AhUhuDW_jOw")
# Movie instance 5
boondock_saints = media.Movie("The Boondock Saints",
                              "Fraternal twins set out to rid Boston of the \
                              evil men operating there while being tracked \
                              down by an FBI agent.",
                              "1999",
                              "https://upload.wikimedia.org/wikipedia/en/1/1b/The_Boondock_Saints_poster.jpeg",  # noqa
                              "https://youtu.be/ydXojYfCF3I")
# Movie instance 6
casino = media.Movie("Casino",
                      "Greed, deception, money, power, and murder occur \
                      between two mobster best friends and a trophy wife over \
                      a gambling empire.",
                      "1995",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/d/d8/Casino_poster.jpg/220px-Casino_poster.jpg",  # noqa
                      "https://youtu.be/EJXDMwGWhoA")
# Store movies in a list
movies = [sandlot, mrs_doubtfire, wedding_crashers,
          days_of_thunder, boondock_saints, casino]
# call open_movies_page function to create movie website
fresh_tomatoes.open_movies_page(movies)
