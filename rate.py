data = json.loads('{"Amount":200000, "Rate":10, "Time":24}')

def cumulative_rate(json_object):
    import json
    json_string = json.dumps(json_object)
    responce = json.loads(json_string)
    amount = responce['Amount'] # loan we have
    rate = responce['Rate']
    time = responce['Time']
    Amount = amount * (pow((1 + rate / 100), time))
    Cumulative_interest = Amount - amount
    return Cumulative_interest
cumulative_rate(data)
