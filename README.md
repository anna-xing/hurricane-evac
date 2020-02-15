# hurricane-evac
Purpose: determine if hurricane evacuation is possible

## Front end (HTML, CSS, JS)
- Displays map with route overlay or recommended action

## Back end (Python + Pandas library for database)
Store user-inputted evac routes in database
Get hurricane path
- Scrape web for time and lat+long coordinates
- Get speed: find distance between lat+long coordinates and divide by time
- Calculate hurricane radius
- Store impacted area

See if user should evacuate
- Check hurricane windspeed: minimum 96 mph
- Call Maps API to get user location from address input
- See if location is in impacted area

If user should evacuate:
- Find time at which hurricane will reach user (interpolate)
- 
