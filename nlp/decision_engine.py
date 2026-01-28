INTENT_REQUIRED_FIELDS = {
    'BOOK_PICKUP' : ['pickup_location', 'drop_location', 'pickup_time'],
    'CHECK_RATE' : ['weight_kg'],
    'TRACK_ORDER' : ['awb_number'],
    'CANCEL_ORDER' : ['awb_number'],
    'RESCHEDULE_PICKUP' : ['pickup_time']
}

def decide_next_action(intent, entities):
    """
    Determines the next action based on intent and extracted entities.
    """
    # 1. Check if intent has mandatory fields
    required_fields = INTENT_REQUIRED_FIELDS.get(intent, [])
    missing_fields = []

    for field in required_fields:
        if not entities.get(field):
            missing_fields.append(field)
    
    # 2. If something is missing -> ask user
    if missing_fields:
        return {
            'next_action': 'ASK_MISSING_FIELDS',
            'missing_fields': missing_fields
        }
    # 3. Intent-specific actions
    if intent == 'RAISE_COMPLAINT':
        return{
            'next_action' : 'CREATE_COMPLAINT_TICKET',
            'ticket_type' : 'DELIVERY_ISSUE'
        }
    
    if intent == 'CONNECT_TO_AGENT':
        return {
            'next_action' : 'HANDOFF_TO_AGENT'
        }
    
    if intent == 'DOCUMENT_UPLOAD_QUERY':
        return {
            'next_action' : 'REQUEST_DOCUMENT_UPLOAD'
        }
    
    
    if intent == 'PAYMENT_QUERY':
        return {
            'next_action' : 'PROVIDE_PAYMENT_INFO'
        }
    
    # 4. Default safe action
    return {
        'next_action': 'PROCEED'
    }
