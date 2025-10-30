# 🗺️ Map Buttons Location Guide

## Where to Find Map Buttons in Your GUI Application

### 1. **Quick Map Test Button** (NEW!)
- **Location**: Top row, next to the Voice button
- **Button Text**: `🗺️ Quick Map Test`  
- **Color**: Orange background
- **Purpose**: Quick test to verify map functionality works
- **Usage**: Click this button for an instant map test with Mumbai, India

### 2. **Main Map Section** 
- **Location**: Bottom of the application window (scroll down if needed)
- **Section Title**: `🏥 🗺️ Find Nearby Hospitals & Medical Shops`
- **Background**: Light green background to make it prominent

### 3. **Map Buttons in Main Section**:

#### **Show on Map Button**
- **Button Text**: `🗺️ Show on Map`
- **Color**: Blue background
- **Location**: Right side of location input area
- **Requirements**: 
  - Enter location (e.g., "Mumbai, India")
  - Select radius (1-20 km)
  - Click button

#### **Open Last Map Button**  
- **Button Text**: `📂 Open Last Map`
- **Color**: Green background
- **Location**: Next to "Show on Map" button
- **Purpose**: Opens previously created map file

## How to Use Map Feature:

### Method 1: Quick Test
1. Click the `🗺️ Quick Map Test` button (orange, top area)
2. Confirm the dialog box
3. Map will be created and opened automatically

### Method 2: Custom Location
1. Scroll down to the green "Find Nearby Hospitals" section
2. Enter your location in the "📍 Your Location" field
3. Select radius from "🔍 Radius (km)" dropdown
4. Click `🗺️ Show on Map` (blue button)

### Method 3: Open Previous Map
1. Click `📂 Open Last Map` (green button)
2. Opens the last created map in your browser

## Troubleshooting:

### If buttons are not visible:
1. **Resize the window** - Make it larger (1200x900 minimum)
2. **Scroll down** - Map section is at the bottom
3. **Look for the green section** - "Find Nearby Hospitals & Medical Shops"

### If map doesn't open:
1. Check if `nearby_places_map.html` file is created
2. Try the "Open Last Map" button
3. Manually open the HTML file in your browser

## File Locations:
- **Map File**: `C:\Codes\csp\nearby_places_map.html`
- **Application**: `C:\Codes\csp\disease_info.py`

## Recent Improvements:
✅ Increased window size to 1200x900  
✅ Made map section more prominent with green background  
✅ Added Quick Map Test button for easy testing  
✅ Enhanced button styling and size  
✅ Improved location input field styling  

---
**Note**: The map functionality creates interactive HTML maps using OpenStreetMap and displays sample hospital/pharmacy locations. For production use, integrate with real APIs like Google Places or Overpass API.