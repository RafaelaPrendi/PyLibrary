# PyLibrary
# To run this web app :
  1.  Download the code
  2.  Run the populate_db.py file inside scripts folder to populate Liber, Autor tables with data from books.csv
  3.  Run the populate_rating.py file inside scripts folder to populate Rating table with data from ratings.csv
 Rating table has user, liber, rating fields. populate_rating.py also creates users with random string as username and 'django1234' as password
# The workflow is:
  1. Login or register user
  2. Search a book from the search bar on the navbar or from the url like "http://127.0.0.1:8000/home/libra/6/"
  3. Add the book to "librat e mi". The  books are added to Profil table that has the fields : user, librat
  4. Repeat process to add several books (you can also remove them from your list)
  5. Click shiko rekomandimet button to view the recommendations or from the url like "http://127.0.0.1:8000/home/rekomandime/"


