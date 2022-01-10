from datetime import datetime
from pytz import timezone

import azure.functions as func

# http://localhost:7071/api/GetSwag?tz=America/Chicago
def main(req: func.HttpRequest) -> func.HttpResponse:
    tz = req.params.get('tz', 'America/Chicago')
    now_utc = datetime.now(timezone(tz))
    weekday, dt, time  = now_utc.strftime("%A|%m/%d/%y|%I:%M %p").split('|')

    output=f"""
    <html>
    <table>
        <tr>
            <th>Weekday</th>
            <th>Date</th>
            <th>Time</th>
        </tr>
        <tr>
            <td>{weekday}</td>
            <td>{dt}</td>
            <td>{time}</td>
        </tr>
    </table>
    </html>  
    """

    return func.HttpResponse(
            output,
            status_code=200,
            mimetype='text/html'
    )

""" POWER BI BLANK QUERY, ADVANCED EDITOR
let
    Source = Web.Page(Web.Contents("http://localhost:7071/api/GetSwag")),
    Data = Source{0}[Data],
    #"Changed Type" = Table.TransformColumnTypes(Data,{{"Weekday", type text}, {"Date", type text}, {"Time", type text}})
in
    #"Changed Type"
"""