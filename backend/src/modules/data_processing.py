import pandas as pd
import numpy as np
import math


recycling_data = {
    "County": [
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Orange County",
        "Orange County",
        "Durham County",
        "Durham County",
    ],
    "City": [
        "Morrisville",
        "Morrisville",
        "Cary",
        "Cary",
        "Apex",
        "Apex",
        "Raleigh",
        "Raleigh",
        "Fuquay-Varina",
        "Fuquay-Varina",
        "Holly Springs",
        "Holly Springs",
        "Garner",
        "Garner",
        "Knightdale",
        "Knightdale",
        "Wendell",
        "Wendell",
        np.nan,
        np.nan,
        np.nan,
        np.nan,
    ],
    "Curbside Recyclable": [
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
    ],
    "Items": [
        "plastic bottles, plastic tubs, plastic jugs, plastic jars, metal cans, glass bottles, glass jars, paper, cartons, cardboard, paper egg cartons, clean pizza boxes",
        "plastic cup lids, plastic straws, single-use cups, rings, to-go containers, scrap metal, mixed metal, ladders, metal pots, metal hangers, mirrors, windows, glassware, greasy pizza boxes, styrofoam egg carton, plastic egg carton, greasy aluminum foil, small pieces of paper, small paper packaging, shredded paper, aerosol cans, batteries, ceramic items, toys, wires",
        "plastic bottles, plastic tubs, plastic jugs, plastic jars, metal cans, glass bottles, glass jars, paper, cartons, cardboard, paper egg cartons, clean pizza boxes",
        "plastic cup lids, plastic straws, single-use cups, rings, to-go containers, scrap metal, mixed metal, ladders, metal pots, metal hangers, mirrors, windows, glassware, greasy pizza boxes, styrofoam egg carton, plastic egg carton, greasy aluminum foil, small pieces of paper, small paper packaging, shredded paper, aerosol cans, batteries, ceramic items, toys, wires",
        "flattened cardboard, glass jars, glass bottles, metal cans, empty aerosol bottles, mixed paper, office paper, glossy paper, post-it notes, envelopes, newspapers, magazines, phonebooks, catalogs, food boxes, paper boxes, paper towel rolls, paper egg carton, paper bags, beverage cartons, plastic cleaning bottles, plastic containers, plastic tubs, plastic bottles",
        "plastic cup lids, plastic straws, single-use cups, rings, to-go containers, scrap metal, mixed metal, ladders, metal pots, metal hangers, mirrors, windows, glassware, greasy pizza boxes, styrofoam egg carton, plastic egg carton, greasy aluminum foil, small pieces of paper, small paper packaging, shredded paper, aerosol cans, batteries, ceramic items, toys, light bulbs, aluminum foil, hardcover books, wires",
        "plastic bottles, plastic tubs, plastic jugs, plastic jars, metal cans, glass bottles, glass jars, paper, cartons, cardboard, paper egg cartons, clean pizza boxes",
        "aerosol can, batteries, aluminium foil, ceramic items, clothing, diapers, electronics, plastic bags, plastic cups, plastic lids, plastic straws, scrap metal, scrap, shredded paper, styrofoam, peanuts, tires, toys, wires",
        "metal cans, flattened cardboard, plastic bottles, plastic jugs, glass bottles, cartons, paper",
        np.nan,
        "corrugated cardboard, food and beverage glass bottles, glass tubs, glass jars, aluminum food trays, metal cans, aseptic containers, cartons, newspapers, magazines, catalogs, paper, paperboard boxes/tubes, plastic bottles, plastic jars, clamshell containers, plastic tubs",
        "greasy pizza boxes, waxed cardboard, non-food glass containers, aerosol cans, non-food metal cans, metal oil cans, metal hangers, checkbooks, carbon paper, used napkins/tissues, used paper plates, waxed paperboard, hardback books, shredded paper, plastic bags, compostable plastic, thin plastic cups, frozen food trays, plastic lids, styrofoam, wires",
        "Aluminum, steel, bi-metal and metal cans, glass bottles, glass jars, paperboard, cardboard, newspapers, magazines, junk mail, catalogs, plastic bottles, plastic tubs, plastic jugs, plastic jars",
        "aerosol cans, batteries, ceramic items, diapers, electronics, food-tainted items, plastic bags, scrap metal, scrap wood, shredded paper, styrofoam, tires, toys, wires",
        "plastic bottles, plastic tubs, plastic jugs, plastic jars, metal cans, glass bottles, glass jars, paper, cartons, cardboard",
        "aerosol cans, aluminum foil, batteries, ceramic items, diapers, disposable cups, electronics, plastic bags, scrap metal, scrap wood, shredded paper, styrofoam, tires, toys, wires",
        "plastic bottles, plastic tubs, plastic jugs, plastic jars, metal cans, glass bottles, glass jars, paper, cartons, cardboard, paper egg cartons, clean pizza boxes, clean aluminum foil",
        "plastic cup lids, plastic straws, single-use cups, rings, to-go containers, scrap metal, mixed metal, ladders, metal pots, metal hangers, mirrors, windows, glassware, greasy pizza boxes, styrofoam egg carton, plastic egg carton, greasy aluminum foil, small pieces of paper, small paper packaging, shredded paper, aerosol cans, batteries, ceramic items, toys, wires",
        "plastic bottles, plastic tubs, plastic jugs, plastic jars, metal cans, glass bottles, glass jars, paper, cartons, cardboard",
        "aerosol cans, aluminum foil, batteries, ceramic items, diapers, disposable cups, electronics, plastic bags, scrap metal, scrap wood, shredded paper, styrofoam, tires, toys, pie pans, metal hangers, household glass, wires",
        "plastic bottles, plastic tubs, plastic jugs, plastic jars, metal cans, paper, cartons, cardboard",
        "aerosol cans, batteries, ceramic items, diapers, electronics, glass bottles, glass jars, household glass, plastic bags, scrap metal, scrap wood, shredded paper, styrofoam, wires, tires, toys",
    ],
}

recycling_df = pd.DataFrame(recycling_data)
recycling_split = recycling_df["Items"].str.split(", ", expand=True)
recycling_split.columns = [f"Item_{i+1}" for i in range(recycling_split.shape[1])]
recycling_df = pd.concat([recycling_df.drop(columns="Items"), recycling_split], axis=1)
recycling_df_filtered = recycling_df[recycling_df["Curbside Recyclable"] != "No"]


waste_data = {
    "County": [
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Wake County",
        "Orange County",
        "Orange County",
        "Orange County",
        "Orange County",
        "Orange County",
        "Durham County",
    ],
    "Center": [
        "Site 1",
        "Site 2",
        "Site 3",
        "Site 4",
        "Site 5",
        "Site 6",
        "Site 7",
        "Site 8",
        "Site 9",
        "Site 10",
        "Site 11",
        "Eubanks Rd. Chapel Hill",
        "Walnut Grove Church Rd. Hillsborough",
        "Bradshaw Quarry Rd. Mebane",
        "Ferguson Rd. Chapel Hill",
        "High Rock Rd. Efland",
        "SWM Convenience Center",
    ],
    "Address": [
        "10505 Old Stage Road, Raleigh, NC 27603",
        "6120 Old Smithfield Road, Apex, NC 27539",
        "266 Aviation Parkway, Morrisville, NC 27560",
        "3600 Yates Mill Pond Road, Raleigh, NC 27606",
        "8401 Battle Bridge Road, Raleigh, NC 27610",
        "3913 Lillie Liles Road, Wake Forest, NC 27587",
        "9024 Deponie Drive, Raleigh, NC 27614",
        "2001 Durham Road / Highway 98, Wake Forest, NC 27587",
        "3337 New Hill-Holleman Road, New Hill, NC 27562",
        "5216 Knightdale-Eagle Rock Road, Knightdale, NC 27545",
        "5051 Wendell Boulevard/Business 64, Wendell, NC 27591",
        "1518 Eubanks Rd. Chapel Hill, NC, 27516",
        "3605 Walnut Grove Church Rd., Hillsborough, NC, 27278",
        "6705 Bradshaw Quarry Rd, Mebane, 27302",
        "1616 Ferguson Rd, Chapel Hill, 27516",
        "7001 High Rock Rd, Efland, 27243",
        "2115 E Club Boulevard Durham, NC 27704",
    ],
    "Items": [
        "electronics (weekends only), household construction debris (homeowner verification required), mattress, box spring, cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "food waste, household construction debris (homeowner verification required), mattress, box spring, cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "electronics (weekends only), food waste, household construction debris (homeowner verification required), mattress, box spring, cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "food waste, household construction debris (homeowner verification required), mattress, box spring, cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "household construction debris (homeowner verification required), cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "electronics (weekends only), household construction debris (homeowner verification required), mattress, box spring, cardboard, clothing, shoes, garbage, mixed recycling, oyster shells, scrap metal",
        "single stream recycling, corrugated cardboard, large rigid plastics, motor oil, oil filters, antifreeze, batteries, electronics, scrap metal, appliances, tires, yard waste, clean wood, food waste, clothing, textiles, shoes, used cooking oil, plastic bags, film",
        "single stream recycling, corrugated cardboard, large rigid plastics, motor oil, oil filters, antifreeze, batteries, electronics, scrap metal, appliances, tires, yard waste, clean wood, food waste, clothing, textiles, shoes, used cooking oil, plastic bags, film",
        "single stream recycling, corrugated cardboard, large rigid plastics, motor oil, oil filters, antifreeze, batteries, electronics, scrap metal, appliances, tires, clean wood",
        "single stream recycling, corrugated cardboard, large rigid plastics, motor oil, oil filters, antifreeze, batteries, electronics, scrap metal, appliances, tires, yard waste, clean wood",
        "single stream recycling, corrugated cardboard, large rigid plastics, motor oil, oil filters, antifreeze, batteries, electronics, scrap metal, appliances, tires, yard waste, clean wood, food waste, clothing, textiles, shoes, used cooking oil",
        "aerosol cans, fire extinguisher, fluorescent light bulbs, garden chemicals, fertilizers, gasoline, household cleaners, batteries, mercury thermometers, oil based paints, petroleum based products, road flares, cooking oil, motor oil, and antifreeze, electronic waste, car battery",
    ],
    "Latitude": [
        35.626478,
        35.683996,
        35.826536,
        35.716226,
        35.714661,
        35.9066005,
        35.9058927,
        35.979464,
        35.6647776,
        35.7872412,
        35.7984545,
        35.9695062,
        36.1440382,
        35.9782699,
        35.8978019,
        36.1367322,
        36.0306617,
    ],
    "Longitude": [
        -78.676878,
        -78.843271,
        -78.818520,
        -78.690102,
        -78.491571,
        -78.5002774,
        -78.5811555,
        -78.5937719,
        -78.9287589,
        -78.4552835,
        -78.3456566,
        -79.0806132,
        -79.1208396,
        -79.2329132,
        -79.1557292,
        -79.2302413,
        -78.8600577,
    ],
}


waste_center = pd.DataFrame(waste_data)
waste_center_split = waste_center["Items"].str.split(", ", expand=True)
waste_center_split.columns = [f"Item_{i+1}" for i in range(waste_center_split.shape[1])]
waste_center_split = pd.concat(
    [
        waste_center[["County", "Center", "Address", "Latitude", "Longitude"]],
        waste_center_split,
    ],
    axis=1,
)


def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Radius of Earth in kilometers (mean radius)
    R = 6371.0
    # Calculate the distance
    return R * c


def check_item_in_city(county, city, item, lat, long):
    # get rows for specified city
    city_data = recycling_df_filtered[recycling_df_filtered["City"] == city]
    # check if any of the columns contain the item
    item_columns = city_data.columns[3:]
    contains_item = city_data[item_columns].apply(
        lambda row: row.str.contains(item, case=False, na=False).any(), axis=1
    )
    # if its within the guidelines we display:
    if contains_item.any():
        return "You can place this in your curbside recycling!"

    # get rows for specified county
    county_data = waste_center_split[waste_center_split["County"] == county]
    # check if any of the columns contain the item
    center_columns = county_data.columns[3:]
    contains_item_in_center = county_data[center_columns].apply(
        lambda row: row.str.contains(item, case=False, na=False).any(), axis=1
    )
    matching_centers = county_data[contains_item_in_center]

    if len(matching_centers) > 0:
        # calculating the closest waste center
        closest_center = None
        closest_distance = float("inf")
        for _, center_row in matching_centers.iterrows():
            center_lat = center_row["Latitude"]
            center_lon = center_row["Longitude"]
            center_name = center_row["Center"]
            address = center_row["Address"]
            distance = haversine(lat, long, center_lat, center_lon)
            if distance < closest_distance:
                closest_distance = distance
                closest_center = (center_name, address)
        # if the item can go to a waste center we display:
        if closest_center:
            return f"You cannot place your {item} in the curbside recycling. However, you may drop it off at your nearest waste {closest_center[0]}. {closest_center[0]} is located at {closest_center[1]}."

    # if the item cannot be recycled nearby or needs to be trashed we display:
    return "This item cannot be recycled in your area!"


def find_county_by_city(city):
    city_data = recycling_df[recycling_df["City"] == city]
    if not city_data.empty:
        return city_data["County"].iloc[0]
    return None
