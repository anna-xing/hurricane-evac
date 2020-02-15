# hurricane-evac
Purpose: determine if hurricane evacuation is possible

## Front end (HTML, CSS, JS)
- Call Maps API to display location
- Displays map with route overlay or recommended action

## Back end (Python + Pandas library for database)
Store user-inputted evac routes in database
Get hurricane path
- Scrape web for time and lat+long coordinates - Rene
- Get speed: find distance between lat+long coordinates and divide by time
- Calculate hurricane radius - Hemika
- Store impacted area

See if user should evacuate
- Call Maps API to get user location from address input
- See if location is in impacted area
- Find time at which hurricane will reach user (interpolate)
- Check hurricane windspeed: minimum 96 mph

If user needs to evacuate...
- Get corresponding route from database, pass into front end display
