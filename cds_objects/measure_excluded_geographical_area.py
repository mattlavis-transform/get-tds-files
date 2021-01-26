from classes.master import Master
import csv


class MeasureExcludedGeographicalArea(Master):

    def __init__(self, md_file, elem):
        Master.__init__(self, elem)
        self.elem = elem
        self.md_file = md_file
        self.get_data()

    def get_data(self):
        if self.operation != "D":
            self.geographical_area_id = Master.process_null(self.elem.find("geographicalArea/geographicalAreaId"))
        else:
            self.geographical_area_id = None
