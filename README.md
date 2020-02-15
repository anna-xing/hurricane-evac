# hurricane-evac
Purpose: determine if hurricane evacuation is possible

## Front end (HTML, CSS, JS)
- User inputs their address
- Call Maps API to display a map of user area
- If user needs to evacuate, then get evac route from database + overlay it

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
