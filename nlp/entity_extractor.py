import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_pickup_time(text):
    text = text.lower()
    if 'tomorrow' in text or 'kal' in text:
        return 'TOMORROW'
    if 'today' in text or 'aaj' in text:
        return 'TODAY'
    if 'morning' in text or 'subah' in text:
        return 'MORNING' 
    return None

def clean_location_text(text):
    remove_words = [
        'pickup', 'kal', 'today', 'tomorrow', 'aaj',
        'morning', 'subah', 'se', 'from', 'to', 'tak',
        'drop', 'location', 'address', 'at', 'in', 'par', 'pe'
    ]
    # remmove whole words only
    for word in remove_words:
        text = re.sub(rf'\b{word}\b', '', text, flags=re.IGNORECASE)
    
    #normalize spaces 
    text = re.sub(r'\s+', ' ', text)
    return text.strip().title()
                    
def extract_entities(text):
    text_lower = text.lower()

    entities = {
        'pickup_time': None,
        'drop_location': None,
        'weight_kg' : None,
        'packages' : None,
        'fragile': False,
        'payment_mode': None,
        'phone_number': None
    }
    weight = re.search(r'(\d+(\.\d+)?)\s?kg', text_lower)
    if weight:
        entities['weight_kg'] = int(weight.group(1))

    # Packages
    packages = re.search(r'(\d+)\s?(package|packages|parcel|parcels|box|boxes)', text_lower)
    if packages:
        entities['packages'] = int(packages.group(1))

    # Fragile
    if 'fragile' in text_lower or 'handle with care' in text_lower or 'glass' in text_lower:        
        entities['fragile'] = True

    # COD
    if 'cod' in text_lower or 'cash on delivery' in text_lower:
        entities['payment_mode'] = 'COD'
    elif 'prepaid' in text_lower or 'paid' in text_lower:
        entities['payment_mode'] = 'PREPAID'

    # Phone number
    phone = re.search(r'(\+91[\-\s]?)?[0]?(91)?[789]\d{9}', text_lower)
    if phone:
        entities['phone_number'] = phone.group(0)

    if 'se' in text_lower and ('pickup' in text_lower or 'le jao' in text_lower):
        parts = text_lower.split('se')

        pickup_raw = parts[0]
        drop_raw = parts[1]

        entities['pickup_location'] = clean_location_text(pickup_raw)
        entities['drop_location'] = clean_location_text(drop_raw)

    entities['pickup_time'] = extract_pickup_time(text)
    return entities

# example input
# print(extract_entities("pickup kal morning Andheri se Powai"))
