# hurricane-evac
Purpose: Hurricane Evac determines if hurricane evacuation is possible from a user-inputted location, and provides recommended next steps.

## Front end (HTML, CSS, JS)
- Home page: Description, button leading to application
- Google Maps API to display a map of user area
- My Maps overlay consisting of evacuation routes in Collier County, Florida
- Evacuation Info button for pop-up recommendations

## Back end (Python with Flask and various libraries, MongoDB)
- Python with Pandas and BeautifulSoup for web scraping National Hurricane Center website
- Python with various mathematical libraries for calculating hurricane trajectory from discrete data points, and determining whether evacuation is necessary
- Flask framework and AJAX calls to link front-end JS and back-end Python scripts
- MongoDB for storing and retrieving custom evacuation routes
