# hurricane-evac
Purpose: Hurricane Evac determines if hurricane evacuation is possible from inputted location, and provide recommended next steps.

## Front end (HTML, CSS, JS)
- Home page: Description, button leading to application
- Google Maps API to display a map of user area
- My Maps overlay consisting of evacuation routes in Collier County, Florida
- Evacuation Info button for pop-up recommendations

## Back end (Python + Pandas library for database)
Store user-inputted evac routes in database

Get hurricane path
- Scrape web for time and lat+long coordinates - Rene
- Get speed: find distance between lat+long coordinates and divide by time - Hemika
- Calculate hurricane radius - Hemika
- Store impacted area

See if user should evacuate
- Pass in user location from front-end JS (format: lat + long)
- See if location is within hurricane radius from hurricane path
- Find time at which hurricane will reach user (interpolate)
- Check hurricane windspeed: minimum 96 mph

If user needs to evacuate...
- Get corresponding route from database, pass into front end display
