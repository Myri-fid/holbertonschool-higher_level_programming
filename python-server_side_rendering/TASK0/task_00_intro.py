#!/usr/bin/env python3
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template
        output = output.replace("{name}", attendee.get("name", "N/A"))
        output = output.replace("{event_title}", attendee.get("event_title", "N/A"))
        output = output.replace("{event_date}", str(attendee.get("event_date", "N/A")))
        output = output.replace("{event_location}", attendee.get("event_location", "N/A"))

        if os.path.exists(f"output_{index}.txt"):
            print(f"Warning: output_{index}.txt already exists. Overwriting.")

        with open(f"output_{index}.txt", "w") as file:
            file.write(output)
