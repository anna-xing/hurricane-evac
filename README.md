# hurricane-evac
Purpose: determine if hurricane evacuation is possible

## Front end (HTML, CSS, JS)
- Displays map with route overlay or recommended action

## Back end (Python + Pandas library for database)
- Database stores user-inputted evac routes
- Call Maps API to get user location
- Scrape hurricane path from web -- determine if user's location is in disaster area, find time until hurricane hits
- Call Maps API and reference db to determine evac travel time + determine if evac is possible
