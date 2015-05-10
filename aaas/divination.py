import signs


def get_base_reading(parsed_date):

    response = {}
    response['source'] = {}

    date = {
        'year': parsed_date.year,
        'month': parsed_date.month,
        'day': parsed_date.day
    }

    response['source']['date'] = date
    response['source']['humanized'] = parsed_date.humanize()
    response['source']['verbose']  = parsed_date.format('dddd MMMM D, YYYY')

    sun_sign = signs.get_sign(parsed_date.month, parsed_date.day)

    if sun_sign is None:
        raise Exception("Problem retrieving sign for %s, %s" % parsed_date.month, parsed_date.day)

    response['signs'] = {}

    response['signs']['sun'] = sun_sign._asdict()

    return response