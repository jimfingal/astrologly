import signs


def get_base_reading(parsed_date):

    response = {}
    response['source'] = get_source_info(parsed_date)

    sun_sign = signs.get_sign(parsed_date.month, parsed_date.day)

    if sun_sign is None:
        raise Exception("Problem retrieving sign for %s, %s" % parsed_date.month, parsed_date.day)

    response['signs'] = {}
    response['signs']['sun'] = sun_sign._asdict()

    return response


def get_full_reading(parsed_date):
    response = {}
    response['source'] = get_source_info(parsed_date)

    sun_sign = signs.get_sign(parsed_date.month, parsed_date.day)
    
    if sun_sign is None:
        raise Exception("Problem retrieving sign for %s, %s" % parsed_date.month, parsed_date.day)

    rising_sign = signs.get_rising_sign(sun_sign, parsed_date.hour, parsed_date.minute)
    
    response['signs'] = {}
    response['signs']['sun'] = sun_sign._asdict()
    response['signs']['rising'] = rising_sign._asdict()

    return response


def get_source_info(parsed_date):

    source = {}

    date = {
        'year': parsed_date.year,
        'month': parsed_date.month,
        'day': parsed_date.day
    }

    source['date'] = date
    source['humanized'] = parsed_date.humanize()
    source['verbose']  = parsed_date.format('dddd MMMM D, YYYY')

    return source
