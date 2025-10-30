# 🗺️ Map Feature Guide

## How to Use the Hospital/Pharmacy Finder

### Step-by-Step Instructions:

1. **Enter Your Location**
   - Type your location in the "Your Location" field
   - Examples: 
     - `Mumbai, India`
     - `Delhi`
     - `Chennai, India`
     - `Bangalore, Karnataka`

2. **Select Search Radius**
   - Choose from dropdown: 1, 2, 5, 10, 15, or 20 km
   - Default: 5 km

3. **Generate Map**
   - Click **"🗺️ Show on Map"** button
   - Wait for status message: "✅ Map created!"
   - Map will automatically open in your default web browser

4. **View Map** (if it doesn't open automatically)
   - Click **"📂 Open Last Map"** button
   - OR double-click `nearby_places_map.html` in project folder
   - OR manually navigate to: `C:\Codes\csp\nearby_places_map.html`

---

## Map Elements

### Markers:
- 🔴 **Red Marker** = Your Location (home icon)
- 🔵 **Blue Markers** = Hospitals & Clinics (plus icon)
- 🟢 **Green Markers** = Pharmacies & Medical Shops (medkit icon)

### Other Features:
- ⭕ **Blue Circle** = Search radius boundary
- **Click markers** to see details (name, type, distance)
- **Zoom** using mouse wheel or +/- buttons
- **Pan** by clicking and dragging the map

---

## Sample Data Notice

⚠️ **IMPORTANT**: The current version shows **SAMPLE/DEMO locations** only!

The hospitals and pharmacies shown are:
- Randomly placed around your location
- Not real facilities
- For demonstration purposes only

### To Get Real Data:
Integrate one of these APIs:
1. **Overpass API** (OpenStreetMap - Free)
2. **Google Places API** (Requires API key)
3. **Healthcare facility databases**

---

## Troubleshooting

### Map doesn't open in browser?
1. Check if file exists: `nearby_places_map.html` in project folder
2. Try clicking **"📂 Open Last Map"** button
3. Manually double-click the HTML file
4. Check your default web browser settings

### Location not found?
- Use format: "City, Country" (e.g., "Mumbai, India")
- Check spelling
- Try major cities first
- Ensure internet connection (for geocoding)

### Map is blank?
- Check internet connection (needed for OpenStreetMap tiles)
- Wait a few seconds for map to load
- Refresh the browser page

---

## File Information

**File Name**: `nearby_places_map.html`
**Location**: `C:\Codes\csp\`
**File Type**: HTML (opens in any web browser)
**Technology**: Folium (Python) + Leaflet.js + OpenStreetMap

---

## Future Enhancements

Planned features:
- [ ] Real hospital data via API integration
- [ ] Filter by facility type (emergency, pharmacy, clinic)
- [ ] Save favorite locations
- [ ] Directions to selected facility
- [ ] Current location detection (GPS)
- [ ] Mobile-responsive design

---

**Made with Folium & OpenStreetMap** 🗺️
