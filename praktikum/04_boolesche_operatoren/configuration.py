from IPython.display import display
import ipywidgets as widgets

elements = {
    "minimum_temperature": None,
    "heat_checkboxes": [],
    "time_range_slider": [],
    "comfort_temperature": []
}

WOCHENTAGE = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

def checkbox_changed(a):
    idx = WOCHENTAGE.index(a["owner"].description)
    elements["time_range_slider"][idx].disabled = not elements["heat_checkboxes"][idx].value
    elements["comfort_temperature"][idx].disabled = not elements["heat_checkboxes"][idx].value

def get_starting_time(weekday):
    idx = WOCHENTAGE.index(weekday)
    return elements["time_range_slider"][idx].value[0]

def get_end_time(weekday):
    idx = WOCHENTAGE.index(weekday)
    return elements["time_range_slider"][idx].value[1]

def is_heating_desired(weekday):
    idx = WOCHENTAGE.index(weekday)
    return elements["heat_checkboxes"][idx].value

def get_soll_temperature(weekday):
    idx = WOCHENTAGE.index(weekday)
    return elements["comfort_temperature"][idx].value

def get_minimum_temperature():
    return elements["minimum_temperature"].value

def show_gui():
    elements["minimum_temperature"] = widgets.BoundedFloatText(
        value=16.0,
        min=3,
        max=30.0,
        step=0.1,
        description='Minimale Temperatur des Gebäudes:',
        disabled=False,
        style={'description_width': 'initial'}
    )

    for tag in WOCHENTAGE:
        elements["heat_checkboxes"].append(widgets.Checkbox(
            value=False,
            description=tag,
            disabled=False,
            indent=False
        ))
        elements["heat_checkboxes"][-1].observe(checkbox_changed)

        elements["time_range_slider"].append(widgets.IntRangeSlider(
                value=[6, 18],
                min=0,
                max=24,
                step=1,
                description='Zeit:',
                disabled=True,
                continuous_update=False,
                orientation='horizontal',
                readout=True,
                readout_format='d',
            ))

        elements["comfort_temperature"].append(widgets.BoundedFloatText(
                value=22.0,
                min=3,
                max=30.0,
                step=0.1,
                description='Soll-Temperatur:',
                disabled=True,
                style={'description_width': 'initial'}
            ))

    vstack = []

    display(widgets.HTML("<b>Konfiguration der Heizungszeiten und Temperaturen</b>"))
    display(elements["minimum_temperature"])
    for i in range(len(elements["heat_checkboxes"])):
        vstack.append(widgets.HBox([elements["heat_checkboxes"][i], 
                                    elements["time_range_slider"][i],
                                    elements["comfort_temperature"][i]]))
    display(widgets.VBox(vstack))
