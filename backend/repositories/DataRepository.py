from tkinter import W
from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    @staticmethod
    def read_Device():
        sql = "SELECT * FROM Device"
        result = Database.get_rows(sql)
        return result

    @staticmethod
    def create_temp(DeviceId, GebruikerId, ActieDatum, Waarde, Commentaar):
        sql = "INSERT INTO Historiek (DeviceId, GerbruikerId, ActieDatum, Waarde, Commentaar) VALUES (%s,%s,%s,%s,%s)"
        params = [DeviceId, GebruikerId, ActieDatum, Waarde, Commentaar]
        result = Database.execute_sql(sql, params)
        return result