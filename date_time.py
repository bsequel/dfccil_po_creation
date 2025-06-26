def date_convertion_ss2(input_date):
    from datetime import datetime

    try:
        # Define a list of possible date format strings
        date_formats = ["%d-%m-%y", "%d.%m.%y", "%d.%m.%Y", "%d.%m.%yy", "%d %m %y", "%d %B %Y", "%d %b %Y", "%d-%B-%Y", "%d-%b-%Y", "%d-%B-%y", "%d-%b-%y", "%d %B %y", "%d/%m/%y", "%d/%m/%Y", "%d %b %y", "%d-%m-%Y", "%d.%b.%y", "%d.%b.%Y", "%d/%B/%y", "%d/%b/%y", "%d/%b/%Y"]

        # Iterate through the date formats and try to parse the input date
        for date_format in date_formats:
            try:
                parsed_date = datetime.strptime(input_date, date_format)
                formatted_date = parsed_date.strftime("%d.%m.%Y")
                return formatted_date
            except ValueError:
                pass

        # If no format matches, raise an exception
        raise ValueError("Invalid date format")

    except ValueError as e:
        return str(e)