def main():
    d = {
        'city': 'portland',
        'state': 'ME',
        'details': ['Cold', 'Snowy', 'Winter']
    }

    print(d.get('country', 'USA'))
    d['country'] = 'AU'

    w = {
        "weather": {
            "description": "light rain",
            "category": "Rain"
        },
        "wind": {
            "speed": 14,
            "deg": 209
        },
        "units": "imperial",
        "forecast": {
            "temp": 55.62,
            "feels_like": 55.02,
            "pressure": 1013,
            "humidity": 88,
            "low": 53,
            "high": 57
        },
        "location": {
            "city": "Portland",
            "state": "OR",
            "country": "US"
        },
        "rate_limiting": {
            "unique_lookups_remaining": 49,
            "lookup_reset_window": "1 hour"
        }
    }

    print(w.get('forecast').get('temp'))


if __name__ == '__main__':
    main()
