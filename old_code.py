import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
from tkinter import ttk
import csv
import os
import datetime as dt
from PIL import Image, ImageTk


def save_to_log(data_row):
    log_file = 'log_Runsheet.csv'
    log_exists = os.path.exists(log_file)
    with open(log_file, 'a', newline='') as log:
        writer = csv.writer(log)
        if not log_exists:
            writer.writerow(['Log of data'])
        writer.writerow(data_row)


def save_data():
    # Fetch data from input fields
    date = date_entry.get()
    outing_number = outing_number_entry.get()
    time = time_entry.get()
    venue = venue_entry.get()
    driver = driver_entry.get()
    engineer_comments = engineer_comments_entry.get("1.0", "end")
    driver_comments = driver_comments_entry.get("1.0", "end")
    # spin
    FL_hot_pressure = FL_hot_pressure_entry.get()
    FR_hot_pressure = FR_hot_pressure_entry.get()
    RL_hot_pressure = RL_hot_pressure_entry.get()
    RR_hot_pressure = RR_hot_pressure_entry.get()
    FL_set_pressure = FL_set_pressure_entry.get()
    FR_set_pressure = FR_set_pressure_entry.get()
    RL_set_pressure = RL_set_pressure_entry.get()
    RR_set_pressure = RR_set_pressure_entry.get()
    FL_out_temp = FL_out_temp_entry.get()
    FL_in_temp = FL_in_temp_entry.get()
    FL_mid_temp = FL_mid_temp_entry.get()
    FR_out_temp = FR_out_temp_entry.get()
    FR_in_temp = FR_in_temp_entry.get()
    FR_mid_temp = FR_mid_temp_entry.get()
    RL_out_temp = RL_out_temp_entry.get()
    RL_in_temp = RL_in_temp_entry.get()
    RL_mid_temp = RL_mid_temp_entry.get()
    RR_out_temp = RR_out_temp_entry.get()
    RR_in_temp = RR_in_temp_entry.get()
    RR_mid_temp = RR_mid_temp_entry.get()
    track_temp = track_temp_entry.get()
    brake_bias = brake_bias_entry.get()
    fl_rebound = fl_rebound_entry.get()
    fr_rebound = fr_rebound_entry.get()
    rl_rebound = rl_rebound_entry.get()
    rr_rebound = rr_rebound_entry.get()
    fl_compression = fl_compression_entry.get()
    fr_compression = fr_compression_entry.get()
    rl_compression = rl_compression_entry.get()
    rr_compression = rr_compression_entry.get()

    # drop
    FW_angle = FW_angle_entry.get()
    camber = camber_entry.get()
    toe = toe_entry.get()
    pedal_box_throttle_position = pedal_box_throttle_position_entry.get()
    pedal_box_brake_position = pedal_box_brake_position_entry.get()
    spring_rates = spring_rates_entry.get()
    ARB_setting = ARB_setting_entry.get()
    differential_ramp_angle = differential_ramp_angle_entry.get()
    R_wing_angle = R_wing_angle_entry.get()

    # input
    FL_corner_weight = FL_corner_weight_entry.get()
    FR_corner_weight = FR_corner_weight_entry.get()
    RL_corner_weight = RL_corner_weight_entry.get()
    RR_corner_weight = RR_corner_weight_entry.get()
    R_ride_height = R_ride_height_entry.get()
    F_ride_height = F_ride_height_entry.get()

    if date and outing_number and time:
        # Save the data into the main CSV file
        save_latest_entry(date, outing_number, time, venue, driver, engineer_comments, driver_comments, FL_hot_pressure,
                          FR_hot_pressure, RL_hot_pressure, RR_hot_pressure, FL_set_pressure, FR_set_pressure,
                          RL_set_pressure, RR_set_pressure, FL_out_temp, FL_in_temp, FL_mid_temp, FR_out_temp,
                          FR_in_temp, FR_mid_temp, RL_out_temp, RL_in_temp, RL_mid_temp, RR_out_temp, RR_in_temp,
                          RR_mid_temp, track_temp, FW_angle, camber, toe, brake_bias, pedal_box_throttle_position,
                          pedal_box_brake_position, spring_rates, FL_corner_weight, FR_corner_weight, RL_corner_weight,
                          RR_corner_weight, fl_rebound, fr_rebound, rl_rebound, rr_rebound, fl_compression,
                          fr_compression, rl_compression, rr_compression, ARB_setting, differential_ramp_angle,
                          R_ride_height, F_ride_height, R_wing_angle)

        # Save to log
        save_to_log([date, outing_number, time, venue, driver, engineer_comments, driver_comments, FL_hot_pressure,
                     FR_hot_pressure, RL_hot_pressure, RR_hot_pressure, FL_set_pressure, FR_set_pressure,
                     RL_set_pressure, RR_set_pressure, FL_out_temp, FL_in_temp, FL_mid_temp, FR_out_temp, FR_in_temp,
                     FR_mid_temp, RL_out_temp, RL_in_temp, RL_mid_temp, RR_out_temp, RR_in_temp, RR_mid_temp,
                     track_temp, FW_angle, camber, toe, brake_bias, pedal_box_throttle_position,
                     pedal_box_brake_position, spring_rates, FL_corner_weight, FR_corner_weight, RL_corner_weight,
                     RR_corner_weight, fl_rebound, fr_rebound, rl_rebound, rr_rebound, fl_compression, fr_compression,
                     rl_compression, rr_compression, ARB_setting, differential_ramp_angle, R_ride_height, F_ride_height,
                     R_wing_angle])

        # Edit save time message
        timeS = dt.datetime.now().strftime("%I:%M:%S %p")
        save_label.config(text=f"Outing last saved: {timeS}")

        # Show success message and update the dropdown menus
        update_dropdown_options()


def clear_entries():
    date_entry.delete(0, tk.END)
    outing_number_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    venue_entry.delete(0, tk.END)
    driver_entry.delete(0, tk.END)
    engineer_comments_entry.delete(1.0, tk.END)
    driver_comments_entry.delete(1.00, tk.END)
    FL_corner_weight_entry.delete(0, tk.END)
    FR_corner_weight_entry.delete(0, tk.END)
    RL_corner_weight_entry.delete(0, tk.END)
    RR_corner_weight_entry.delete(0, tk.END)
    R_ride_height_entry.delete(0, tk.END)
    F_ride_height_entry.delete(0, tk.END)


def update_selected(*args):
    selected_value = selected_entry.get()
    if selected_value.isdigit() and int(selected_value) in data_indices:
        selected_index = int(selected_value) - 1  # Adjusting the index to match the data list's zero-based index
        selected_row = data[selected_index]  # Retrieve the selected row from data

        # Populate original entry fields with selected data for editing
        clear_entries()

        date_entry.insert(tk.END, selected_row[0])
        outing_number_entry.insert(tk.END, selected_row[1])
        time_entry.insert(tk.END, selected_row[2])
        venue_entry.insert(tk.END, selected_row[3])
        driver_entry.insert(tk.END, selected_row[4])
        engineer_comments_entry.insert(tk.END, selected_row[5])
        driver_comments_entry.insert(tk.END, selected_row[6])
        FL_hot_pressure_var.set(selected_row[7])
        FR_hot_pressure_var.set(selected_row[8])
        RL_hot_pressure_var.set(selected_row[9])
        RR_hot_pressure_var.set(selected_row[10])
        FL_set_pressure_var.set(selected_row[11])
        FR_set_pressure_var.set(selected_row[12])
        RL_set_pressure_var.set(selected_row[13])
        RR_set_pressure_var.set(selected_row[14])
        FL_out_temp_var.set(selected_row[15])
        FL_in_temp_var.set(selected_row[16])
        FL_mid_temp_var.set(selected_row[17])
        FR_out_temp_var.set(selected_row[18])
        FR_in_temp_var.set(selected_row[19])
        FR_mid_temp_var.set(selected_row[20])
        RL_out_temp_var.set(selected_row[21])
        RL_in_temp_var.set(selected_row[22])
        RL_mid_temp_var.set(selected_row[23])
        RR_out_temp_var.set(selected_row[24])
        RR_in_temp_var.set(selected_row[25])
        RR_mid_temp_var.set(selected_row[26])
        track_temp_var.set(selected_row[27])
        FW_angle_entry.set(selected_row[28])
        camber_entry.set(selected_row[29])
        toe_entry.set(selected_row[30])
        brake_bias_var.set(selected_row[31])
        pedal_box_throttle_position_entry.set(selected_row[32])
        pedal_box_brake_position_entry.set(selected_row[33])
        spring_rates_entry.set(selected_row[34])
        FL_corner_weight_entry.insert(tk.END, selected_row[35])
        FR_corner_weight_entry.insert(tk.END, selected_row[36])
        RL_corner_weight_entry.insert(tk.END, selected_row[37])
        RR_corner_weight_entry.insert(tk.END, selected_row[38])
        fl_rebound_var.set(selected_row[39])
        fr_rebound_var.set(selected_row[40])
        rl_rebound_var.set(selected_row[41])
        rr_rebound_var.set(selected_row[42])
        fl_compression_var.set(selected_row[43])
        fr_compression_var.set(selected_row[44])
        rl_compression_var.set(selected_row[45])
        rr_compression_var.set(selected_row[46])
        ARB_setting_entry.set(selected_row[47])
        differential_ramp_angle_entry.set(selected_row[48])
        R_ride_height_entry.insert(tk.END, selected_row[49])
        F_ride_height_entry.insert(tk.END, selected_row[50])
        R_wing_angle_entry.set(selected_row[51])

        # Change the save button command to perform the update instead of saving new data
        save_button.config(command=lambda: update_data(selected_index))

        # Show the editing message
        save_label.config(text="Editing an entry")

        # Hide the "New Outing" button during editing
        new_outing_button.grid_remove()
        cancel_button.grid()



    else:
        messagebox.showwarning("Invalid Selection", "Please select a valid entry to edit.")


def update_data(selected_index):
    # Check if the selected_index is within the valid range of the data list
    if selected_index >= 0 and selected_index < len(data):
        # Get updated data from the input fields
        new_date = date_entry.get()
        new_outing_number = outing_number_entry.get()
        new_time = time_entry.get()
        new_venue = venue_entry.get()
        new_driver = driver_entry.get()
        new_engineer_comments = engineer_comments_entry.get("1.0", "end")
        new_driver_comments = driver_comments_entry.get("1.0", "end")
        # spin
        new_FL_hot_pressure = FL_hot_pressure_entry.get()
        new_FR_hot_pressure = FR_hot_pressure_entry.get()
        new_RL_hot_pressure = RL_hot_pressure_entry.get()
        new_RR_hot_pressure = RR_hot_pressure_entry.get()
        new_FL_set_pressure = FL_set_pressure_entry.get()
        new_FR_set_pressure = FR_set_pressure_entry.get()
        new_RL_set_pressure = RL_set_pressure_entry.get()
        new_RR_set_pressure = RR_set_pressure_entry.get()
        new_FL_out_temp = FL_out_temp_entry.get()
        new_FL_in_temp = FL_in_temp_entry.get()
        new_FL_mid_temp = FL_mid_temp_entry.get()
        new_FR_out_temp = FR_out_temp_entry.get()
        new_FR_in_temp = FR_in_temp_entry.get()
        new_FR_mid_temp = FR_mid_temp_entry.get()
        new_RL_out_temp = RL_out_temp_entry.get()
        new_RL_in_temp = RL_in_temp_entry.get()
        new_RL_mid_temp = RL_mid_temp_entry.get()
        new_RR_out_temp = RR_out_temp_entry.get()
        new_RR_in_temp = RR_in_temp_entry.get()
        new_RR_mid_temp = RR_mid_temp_entry.get()
        new_track_temp = track_temp_entry.get()
        new_brake_bias = brake_bias_entry.get()
        new_fl_rebound = fl_rebound_entry.get()
        new_fr_rebound = fr_rebound_entry.get()
        new_rl_rebound = rl_rebound_entry.get()
        new_rr_rebound = rr_rebound_entry.get()
        new_fl_compression = fl_compression_entry.get()
        new_fr_compression = fr_compression_entry.get()
        new_rl_compression = rl_compression_entry.get()
        new_rr_compression = rr_compression_entry.get()

        # drop
        new_FW_angle = FW_angle_entry.get()
        new_camber = camber_entry.get()
        new_toe = toe_entry.get()
        new_pedal_box_throttle_position = pedal_box_throttle_position_entry.get()
        new_pedal_box_brake_position = pedal_box_brake_position_entry.get()
        new_spring_rates = spring_rates_entry.get()
        new_ARB_setting = ARB_setting_entry.get()
        new_differential_ramp_angle = differential_ramp_angle_entry.get()
        new_R_wing_angle = R_wing_angle_entry.get()

        # inputs
        new_FL_corner_weight = FL_corner_weight_entry.get()
        new_FR_corner_weight = FR_corner_weight_entry.get()
        new_RL_corner_weight = RL_corner_weight_entry.get()
        new_RR_corner_weight = RR_corner_weight_entry.get()
        new_R_ride_height = R_ride_height_entry.get()
        new_F_ride_height = F_ride_height_entry.get()

        # Retrieve the original data to compare changes
        original_entry = data[selected_index]

        # Update the selected entry in the data list
        data[selected_index] = [new_date, new_outing_number, new_time, new_venue,
                                new_driver, new_engineer_comments, new_driver_comments,
                                new_FL_hot_pressure, new_FR_hot_pressure, new_RL_hot_pressure, new_RR_hot_pressure,
                                new_FL_set_pressure, new_FR_set_pressure, new_RL_set_pressure, new_RR_set_pressure,
                                new_FL_out_temp, new_FL_in_temp, new_FL_mid_temp, new_FR_out_temp, new_FR_in_temp,
                                new_FR_mid_temp, new_RL_out_temp, new_RL_in_temp, new_RL_mid_temp, new_RR_out_temp,
                                new_RR_in_temp, new_RR_mid_temp, new_track_temp, new_FW_angle, new_camber, new_toe,
                                new_brake_bias, new_pedal_box_throttle_position, new_pedal_box_brake_position,
                                new_spring_rates, new_FL_corner_weight, new_FR_corner_weight, new_RL_corner_weight,
                                new_RR_corner_weight, new_fl_rebound, new_fr_rebound, new_rl_rebound, new_rr_rebound,
                                new_fl_compression, new_fr_compression, new_rl_compression, new_rr_compression,
                                new_ARB_setting, new_differential_ramp_angle, new_R_ride_height, new_F_ride_height,
                                new_R_wing_angle]

        # Write the updated data back to the CSV file
        with open('Runsheet.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        # Save to log
        save_to_log([new_date, new_outing_number, new_time, new_venue,
                     new_driver, new_engineer_comments, new_driver_comments,
                     new_FL_hot_pressure, new_FR_hot_pressure, new_RL_hot_pressure, new_RR_hot_pressure,
                     new_FL_set_pressure, new_FR_set_pressure, new_RL_set_pressure, new_RR_set_pressure,
                     new_FL_out_temp, new_FL_in_temp, new_FL_mid_temp, new_FR_out_temp, new_FR_in_temp, new_FR_mid_temp,
                     new_RL_out_temp, new_RL_in_temp, new_RL_mid_temp, new_RR_out_temp, new_RR_in_temp, new_RR_mid_temp,
                     new_track_temp, new_FW_angle, new_camber, new_toe, new_brake_bias, new_pedal_box_throttle_position,
                     new_pedal_box_brake_position, new_spring_rates, new_FL_corner_weight, new_FR_corner_weight,
                     new_RL_corner_weight, new_RR_corner_weight, new_fl_rebound, new_fr_rebound, new_rl_rebound,
                     new_rr_rebound, new_fl_compression, new_fr_compression, new_rl_compression, new_rr_compression,
                     new_ARB_setting, new_differential_ramp_angle, new_R_ride_height, new_F_ride_height,
                     new_R_wing_angle, "Originally:", original_entry[0], original_entry[1], original_entry[2]])

        # Show success message, reset entry fields, update the dropdown, and remove the editing message
        messagebox.showinfo("Success", "Data edited successfully!")
        clear_entries()
        update_dropdown_options()
        save_label.config(text="")

        # Show the "New Outing" button dropdown after editing and hide "cancel" button
        new_outing_button.grid()
        cancel_button.grid_remove()

        # After the update is successful, reverts the save_button command back to save_data()
        save_button.config(command=save_data)

    else:
        messagebox.showwarning("Invalid Selection", "Selected entry index out of range.")


def cancel_update():
    clear_entries()
    save_label.config(text="")
    new_outing_button.grid()
    save_button.config(command=save_data)
    cancel_button.grid_remove()


def update_dropdown_options():
    dropdown['menu'].delete(0, 'end')
    data.clear()
    data_indices.clear()

    if os.path.exists('Runsheet.csv') and os.path.getsize('Runsheet.csv') > 0:
        with open('Runsheet.csv', 'r') as file:
            reader = csv.reader(file)
            index = 1  # Start index from 1
            for row in reader:
                data.append(row)
                data_indices[index] = len(data) - 1  # Map index to the row in data
                dropdown['menu'].add_command(label=f"Date: {row[0]}, Outing Number: {row[1]}, Time: {row[2]}",
                                             command=lambda idx=index: selected_entry.set(str(idx)))
                index += 1


def get_previous_outing_number(date):
    previous_outing_number = 0  # Default value if there are no entries for the given date

    if os.path.exists('Runsheet.csv') and os.path.getsize('Runsheet.csv') > 0:
        with open('Runsheet.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == date and row[1].isdigit():
                    previous_outing_number = max(previous_outing_number, int(row[1]))

    return previous_outing_number


def save_latest_entry(date, outing_number, time, venue, driver, engineer_comments, driver_comments, FL_hot_pressure,
                      FR_hot_pressure, RL_hot_pressure, RR_hot_pressure, FL_set_pressure, FR_set_pressure,
                      RL_set_pressure, RR_set_pressure, FL_out_temp, FL_in_temp, FL_mid_temp, FR_out_temp, FR_in_temp,
                      FR_mid_temp, RL_out_temp, RL_in_temp, RL_mid_temp, RR_out_temp, RR_in_temp, RR_mid_temp,
                      track_temp, FW_angle, camber, toe, brake_bias, pedal_box_throttle_position,
                      pedal_box_brake_position, spring_rates, FL_corner_weight, FR_corner_weight, RL_corner_weight,
                      RR_corner_weight, fl_rebound, fr_rebound, rl_rebound, rr_rebound, fl_compression, fr_compression,
                      rl_compression, rr_compression, ARB_setting, differential_ramp_angle, R_ride_height,
                      F_ride_height, R_wing_angle
                      ):
    data_rows = []  # To store all data rows except the last one

    # Fetch all rows except the last one
    if os.path.exists('Runsheet.csv') and os.path.getsize('Runsheet.csv') > 0:
        with open('Runsheet.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data_rows.append(row)

    # Check if there are any existing entries to update
    if data_rows:
        last_entry = data_rows[-1]  # Fetch the last entry

        # Check if the last entry matches the provided date and outing number
        if last_entry[0] == date and last_entry[1] == outing_number:
            last_entry[0] = date
            last_entry[1] = outing_number

            # Write all entries except the last one and then write the updated last entry
            with open('Runsheet.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data_rows[:-1])  # Write all except the last entry
                writer.writerow(
                    [date, outing_number, time, venue, driver, engineer_comments, driver_comments, FL_hot_pressure,
                     FR_hot_pressure, RL_hot_pressure, RR_hot_pressure, FL_set_pressure, FR_set_pressure,
                     RL_set_pressure, RR_set_pressure, FL_out_temp, FL_in_temp, FL_mid_temp, FR_out_temp, FR_in_temp,
                     FR_mid_temp, RL_out_temp, RL_in_temp, RL_mid_temp, RR_out_temp, RR_in_temp, RR_mid_temp,
                     track_temp, FW_angle, camber, toe, brake_bias, pedal_box_throttle_position,
                     pedal_box_brake_position, spring_rates, FL_corner_weight, FR_corner_weight, RL_corner_weight,
                     RR_corner_weight, fl_rebound, fr_rebound, rl_rebound, rr_rebound, fl_compression, fr_compression,
                     rl_compression, rr_compression, ARB_setting, differential_ramp_angle, R_ride_height, F_ride_height,
                     R_wing_angle
                     ])
        else:
            # If no match found, append a new entry
            with open('Runsheet.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    [date, outing_number, time, venue, driver, engineer_comments, driver_comments, FL_hot_pressure,
                     FR_hot_pressure, RL_hot_pressure, RR_hot_pressure, FL_set_pressure, FR_set_pressure,
                     RL_set_pressure, RR_set_pressure, FL_out_temp, FL_in_temp, FL_mid_temp, FR_out_temp, FR_in_temp,
                     FR_mid_temp, RL_out_temp, RL_in_temp, RL_mid_temp, RR_out_temp, RR_in_temp, RR_mid_temp,
                     track_temp, FW_angle, camber, toe, brake_bias, pedal_box_throttle_position,
                     pedal_box_brake_position, spring_rates, FL_corner_weight, FR_corner_weight, RL_corner_weight,
                     RR_corner_weight, fl_rebound, fr_rebound, rl_rebound, rr_rebound, fl_compression, fr_compression,
                     rl_compression, rr_compression, ARB_setting, differential_ramp_angle, R_ride_height, F_ride_height,
                     R_wing_angle
                     ])
    else:
        # If no existing entries, create a new one
        with open('Runsheet.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                [date, outing_number, time, venue, driver, engineer_comments, driver_comments, FL_hot_pressure,
                 FR_hot_pressure, RL_hot_pressure, RR_hot_pressure, FL_set_pressure, FR_set_pressure, RL_set_pressure,
                 RR_set_pressure, FL_out_temp, FL_in_temp, FL_mid_temp, FR_out_temp, FR_in_temp, FR_mid_temp,
                 RL_out_temp, RL_in_temp, RL_mid_temp, RR_out_temp, RR_in_temp, RR_mid_temp, track_temp, FW_angle,
                 camber, toe, brake_bias, pedal_box_throttle_position, pedal_box_brake_position, spring_rates,
                 FL_corner_weight, FR_corner_weight, RL_corner_weight, RR_corner_weight, fl_rebound, fr_rebound,
                 rl_rebound, rr_rebound, fl_compression, fr_compression, rl_compression, rr_compression, ARB_setting,
                 differential_ramp_angle, R_ride_height, F_ride_height, R_wing_angle
                 ])


def get_venue(outing_number, date):
    with open('Runsheet.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            previous_outing_number = str((int(outing_number)) - 1)
            # Check for matching outing number and date in each row
            if row[0] == date and row[1] == previous_outing_number:
                venue = row[3]  # Assuming venue is in the forth column (index 3)
    return venue


def create_new_outing():
    clear_entries()
    # Get the current date and format it
    current_date = dt.datetime.now()
    formatted_date = current_date.strftime("%a, %b %d %Y")

    # Insert the formatted date into the date entry field
    date_entry.insert(tk.END, formatted_date)

    # Fetch the previous outing number for today's date from the CSV
    previous_outing_number = get_previous_outing_number(formatted_date)

    # Increment the previous outing number by 1 or set it to 1 if it's a new date
    new_outing_number = previous_outing_number + 1

    if new_outing_number > 1:
        venue = get_venue(new_outing_number, formatted_date)
        venue_entry.insert(tk.END, venue)

    # Display the updated outing number in the outing number entry field
    outing_number_entry.insert(tk.END, str(new_outing_number))

    # Automatically fill time
    time = dt.datetime.now().strftime("%I:%M %p")
    time_entry.insert(tk.END, time)

    # Save the new entry
    save_data()


# Store data rows from the CSV
data = []
# Initialize data_indices as a dictionary
data_indices = {}

root = tk.Tk()
root.title("Runsheet")

# Set window dimensions
window_width = 1150
window_height = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = 0
y_coordinate = 0

root.geometry(f"{screen_width}x{screen_height}+{x_coordinate}+{y_coordinate}")

# Load Image
image_path = "car.png"
image = Image.open(image_path)

width, height = 400, 300
image.thumbnail((width, height))

# Convert the image for Tkinter
tk_image = ImageTk.PhotoImage(image)
###
# Load Image
image_path3 = "car.png"
image3 = Image.open(image_path3)

width3, height3 = 400, 300
image3.thumbnail((width3, height3))

# Convert the image for Tkinter
tk_image3 = ImageTk.PhotoImage(image3)

logo_path = "logo.png"
logo = Image.open(logo_path)
Lwidth, Lheight = 300, 80
logo.thumbnail((Lwidth, Lheight))

# Convert the image for Tkinter
tk_image2logo = ImageTk.PhotoImage(logo)

# Create a label to display the image
image_label = tk.Label(root, image=tk_image)
image_label.grid(row=5, column=2, rowspan=13, sticky='', pady=85, ipady=70)

# Create a label to display the image
image_label3 = tk.Label(root, image=tk_image3)
image_label3.grid(row=5, column=6, rowspan=13, sticky='e', pady=60, ipady=70)

canvas = tk.Canvas(root, width=1150, height=100)
canvas.grid(row=0, column=0, columnspan=20)

# Draw a horizontal line across the canvas
canvas.create_line(0, 80, 1150, 80, fill="black", width=2)

# Create a label to display the image
logo_label = tk.Label(root, image=tk_image2logo)
logo_label.grid(row=0, column=0, sticky='n', pady=10, padx=10)

title_label = tk.Label(root, text="Runsheet Application", font=Font(size=18, weight='bold'))
title_label.grid(row=0, column=1, sticky='NW', pady=20, columnspan=2)

# Input fields for data entry
date_label = tk.Label(root, text="                                                   Date:                        ")
date_label.grid(row=1, column=0, sticky='w', pady=10)
date_entry = tk.Entry(root, width=37)
date_entry.grid(row=1, column=0, sticky='e')

outing_number_label = tk.Label(root, text="                               Outing Number:")
outing_number_label.grid(row=2, column=0, sticky='w', pady=20)
outing_number_entry = tk.Entry(root, width=37)
outing_number_entry.grid(row=2, column=0, sticky='e')

time_label = tk.Label(root, text="                                                  Time:")
time_label.grid(row=3, column=0, sticky='w', pady=10)
time_entry = tk.Entry(root, width=37)
time_entry.grid(row=3, column=0, sticky='e')

venue_label = tk.Label(root, text="                                                Venue:")
venue_label.grid(row=4, column=0, sticky='w', pady=10)
venue_entry = tk.Entry(root, width=37)
venue_entry.grid(row=4, column=0, sticky='e')

driver_label = tk.Label(root, text="                                                 Driver:")
driver_label.grid(row=5, column=0, sticky='w', pady=10)
driver_entry = tk.Entry(root, width=37)
driver_entry.grid(row=5, column=0, sticky='e')

engineer_comments_label = tk.Label(root, text="                       Engineer Comments:")
engineer_comments_label.grid(row=6, column=0, sticky='w', pady=10)
engineer_comments_entry = tk.Text(root, width=32, height=4, font=Font(family='Helvetica', size=10))
engineer_comments_entry.grid(row=6, column=0, sticky='e', columnspan=1)

driver_comments_label = tk.Label(root, text="                            Driver Comments:")
driver_comments_label.grid(row=7, column=0, sticky='w', pady=10)
driver_comments_entry = tk.Text(root, width=32, height=4, font=Font(family='Helvetica', size=10))
driver_comments_entry.grid(row=7, column=0, sticky='e', columnspan=1)

FL_corner_weight_label = tk.Label(root, text="Front left corner weight:")
FL_corner_weight_label.grid(row=4, column=3, sticky='e', pady=10)
FL_corner_weight_entry = tk.Entry(root)
FL_corner_weight_entry.grid(row=4, column=4, sticky='w')

FR_corner_weight_label = tk.Label(root, text="Front right corner weight:")
FR_corner_weight_label.grid(row=4, column=5, sticky='e', pady=10)
FR_corner_weight_entry = tk.Entry(root)
FR_corner_weight_entry.grid(row=4, column=6, sticky='w')

RL_corner_weight_label = tk.Label(root, text="Rear left corner weight:")
RL_corner_weight_label.grid(row=5, column=3, sticky='e')
RL_corner_weight_entry = tk.Entry(root)
RL_corner_weight_entry.grid(row=5, column=4, sticky='w')

RR_corner_weight_label = tk.Label(root, text="Rear right corner weight:")
RR_corner_weight_label.grid(row=5, column=5, sticky='e')
RR_corner_weight_entry = tk.Entry(root)
RR_corner_weight_entry.grid(row=5, column=6, sticky='w')

R_ride_height_label = tk.Label(root, text="Rear ride height:")
R_ride_height_label.grid(row=6, column=3, sticky='e')
R_ride_height_entry = tk.Entry(root)
R_ride_height_entry.grid(row=6, column=4, sticky='w')

F_ride_height_label = tk.Label(root, text="Front ride height:")
F_ride_height_label.grid(row=6, column=5, sticky='e')
F_ride_height_entry = tk.Entry(root)
F_ride_height_entry.grid(row=6, column=6, sticky='w')

# label for space
space_label = tk.Label(root, text="                                                                           ")
space_label.grid(row=10, column=0, sticky='w', pady=10, padx=100)

FL_hot_pressure_var = tk.IntVar()
FR_hot_pressure_var = tk.IntVar()
RL_hot_pressure_var = tk.IntVar()
RR_hot_pressure_var = tk.IntVar()
FL_set_pressure_var = tk.IntVar()
FR_set_pressure_var = tk.IntVar()
RL_set_pressure_var = tk.IntVar()
RR_set_pressure_var = tk.IntVar()
FL_out_temp_var = tk.IntVar()
FL_in_temp_var = tk.IntVar()
FL_mid_temp_var = tk.IntVar()
FR_out_temp_var = tk.IntVar()
FR_in_temp_var = tk.IntVar()
FR_mid_temp_var = tk.IntVar()
RL_out_temp_var = tk.IntVar()
RL_in_temp_var = tk.IntVar()
RL_mid_temp_var = tk.IntVar()
RR_out_temp_var = tk.IntVar()
RR_in_temp_var = tk.IntVar()
RR_mid_temp_var = tk.IntVar()
track_temp_var = tk.IntVar()
brake_bias_var = tk.IntVar()
fl_rebound_var = tk.IntVar()
fl_compression_var = tk.IntVar()
fr_rebound_var = tk.IntVar()
fr_compression_var = tk.IntVar()
rl_rebound_var = tk.IntVar()
rl_compression_var = tk.IntVar()
rr_rebound_var = tk.IntVar()
rr_compression_var = tk.IntVar()

# Create labels and Spinbox widgets for each variable
FL_set_pressure_label = tk.Label(root, text="Set pressure:")
FL_set_pressure_label.grid(row=7, column=6, sticky='sw', pady=5)

FL_set_pressure_entry = tk.Spinbox(root, from_=10, to=15, width=2, textvariable=FL_set_pressure_var,
                                   font=Font(family='Helvetica', size=17, weight='bold'), bg="black", fg="white")
FL_set_pressure_entry.grid(row=8, column=6, sticky='nw')

# FR_set_pressure
FR_set_pressure_label = tk.Label(root, text="Set Pressure:")
FR_set_pressure_label.grid(row=7, column=6, sticky='se', pady=5)

FR_set_pressure_entry = tk.Spinbox(root, from_=10, to=15, width=2, textvariable=FR_set_pressure_var,
                                   font=Font(family='Helvetica', size=17, weight='bold'), bg="black", fg="white")
FR_set_pressure_entry.grid(row=8, column=6, sticky='ne')

# RL_set_pressure
RL_set_pressure_label = tk.Label(root, text="Set Pressure:")
RL_set_pressure_label.grid(row=9, column=6, sticky='sw')

RL_set_pressure_entry = tk.Spinbox(root, from_=10, to=15, width=2, textvariable=RL_set_pressure_var,
                                   font=Font(family='Helvetica', size=17, weight='bold'), bg="black", fg="white")
RL_set_pressure_entry.grid(row=10, column=6, sticky='nw', pady=10)

# RR_set_pressure
RR_set_pressure_label = tk.Label(root, text="Set Pressure:")
RR_set_pressure_label.grid(row=9, column=6, sticky='es')

RR_set_pressure_entry = tk.Spinbox(root, from_=10, to=15, width=2, textvariable=RR_set_pressure_var,
                                   font=Font(family='Helvetica', size=17, weight='bold'), bg="black", fg="white")
RR_set_pressure_entry.grid(row=10, column=6, sticky='en', pady=10)

# FL_hot_pressure
FL_hot_pressure_label = tk.Label(root, text="Hot pressure:")
FL_hot_pressure_label.grid(row=7, column=2, sticky='ws', pady=5)

FL_hot_pressure_entry = tk.Spinbox(root, from_=10, to=15, width=2, textvariable=FL_hot_pressure_var,
                                   font=Font(family='Helvetica', size=17, weight='bold'), bg="black", fg="white")
FL_hot_pressure_entry.grid(row=8, column=2, sticky='nw')

# FR_hot_pressure
FR_hot_pressure_label = tk.Label(root, text="Hot pressure:")
FR_hot_pressure_label.grid(row=7, column=2, sticky='es', pady=5)

FR_hot_pressure_entry = tk.Spinbox(root, from_=10, to=15, width=2, textvariable=FR_hot_pressure_var,
                                   font=Font(family='Helvetica', size=17, weight='bold'), bg="black", fg="white")
FR_hot_pressure_entry.grid(row=8, column=2, sticky='ne')

# RL_hot_pressure
RL_hot_pressure_label = tk.Label(root, text="Hot pressure:")
RL_hot_pressure_label.grid(row=9, column=2, sticky='sw')

RL_hot_pressure_entry = tk.Spinbox(root, from_=10, to=15, width=2, textvariable=RL_hot_pressure_var,
                                   font=Font(family='Helvetica', size=17, weight='bold'), bg="black", fg="white")
RL_hot_pressure_entry.grid(row=10, column=2, sticky='nw', pady=10)

# RR_hot_pressure
RR_hot_pressure_label = tk.Label(root, text="Hot pressure:")
RR_hot_pressure_label.grid(row=9, column=2, sticky='se')

RR_hot_pressure_entry = tk.Spinbox(root, from_=10, to=15, width=2, textvariable=RR_hot_pressure_var,
                                   font=Font(family='Helvetica', size=17, weight='bold'), bg="black", fg="white")
RR_hot_pressure_entry.grid(row=10, column=2, sticky='ne', pady=10)

# temp label
temp_label = tk.Label(root, text="Temperature", font=Font(size=10, weight='bold'))
temp_label.grid(row=7, column=1, sticky='we', padx=27)

# FL_out_temp
FL_out_temp_label = tk.Label(root, text="Outer:")
FL_out_temp_label.grid(row=7, column=1, sticky='sw', pady=5, padx=0)

FL_out_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=FL_out_temp_var,
                               font=Font(family='Helvetica', size=17, weight='bold'))
FL_out_temp_entry.grid(row=8, column=1, sticky='nw', padx=0)

# FL_in_temp
FL_in_temp_label = tk.Label(root, text="Inner:")
FL_in_temp_label.grid(row=7, column=1, sticky='es', pady=5)

FL_in_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=FL_in_temp_var,
                              font=Font(family='Helvetica', size=17, weight='bold'))
FL_in_temp_entry.grid(row=8, column=1, sticky='en')

# FL_mid_temp
FL_mid_temp_label = tk.Label(root, text="Middle:")
FL_mid_temp_label.grid(row=7, column=1, sticky='s', pady=5)

FL_mid_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=FL_mid_temp_var,
                               font=Font(family='Helvetica', size=17, weight='bold'))
FL_mid_temp_entry.grid(row=8, column=1, sticky='n', padx=0)

# temp label
temp2_label = tk.Label(root, text="Temperature", font=Font(size=10, weight='bold'))
temp2_label.grid(row=7, column=3, sticky='')

# FR_out_temp
FR_out_temp_label = tk.Label(root, text="Outer:")
FR_out_temp_label.grid(row=7, column=3, sticky='es', pady=5)

FR_out_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=FR_out_temp_var,
                               font=Font(family='Helvetica', size=17, weight='bold'))
FR_out_temp_entry.grid(row=8, column=3, sticky='ne')

# FR_in_temp
FR_in_temp_label = tk.Label(root, text="Inner:")
FR_in_temp_label.grid(row=7, column=3, sticky='sw', pady=5)

FR_in_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=FR_in_temp_var,
                              font=Font(family='Helvetica', size=17, weight='bold'))
FR_in_temp_entry.grid(row=8, column=3, sticky='nw')

# FR_mid_temp
FR_mid_temp_label = tk.Label(root, text="Middle:")
FR_mid_temp_label.grid(row=7, column=3, sticky='s', pady=5)

FR_mid_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=FR_mid_temp_var,
                               font=Font(family='Helvetica', size=17, weight='bold'))
FR_mid_temp_entry.grid(row=8, column=3, sticky='n')

# temp label
temp3_label = tk.Label(root, text="Temperature", font=Font(size=10, weight='bold'))
temp3_label.grid(row=9, column=1, sticky='')

# RL_out_temp
RL_out_temp_label = tk.Label(root, text="Outer:")
RL_out_temp_label.grid(row=9, column=1, sticky='ws')

RL_out_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=RL_out_temp_var,
                               font=Font(family='Helvetica', size=17, weight='bold'))
RL_out_temp_entry.grid(row=10, column=1, sticky='wn', pady=10)

# RL_in_temp
RL_in_temp_label = tk.Label(root, text="Inner:")
RL_in_temp_label.grid(row=9, column=1, sticky='se')

RL_in_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=RL_in_temp_var,
                              font=Font(family='Helvetica', size=17, weight='bold'))
RL_in_temp_entry.grid(row=10, column=1, sticky='ne', pady=10)

# RL_mid_temp
RL_mid_temp_label = tk.Label(root, text="Middle:")
RL_mid_temp_label.grid(row=9, column=1, sticky='s', padx=30)

RL_mid_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=RL_mid_temp_var,
                               font=Font(family='Helvetica', size=17, weight='bold'))
RL_mid_temp_entry.grid(row=10, column=1, sticky='n', pady=10)

# temp label
temp3_label = tk.Label(root, text="Temperature", font=Font(size=10, weight='bold'))
temp3_label.grid(row=9, column=3, sticky='')

# RR_out_temp
RR_out_temp_label = tk.Label(root, text="Outer:")
RR_out_temp_label.grid(row=9, column=3, sticky='se')

RR_out_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=RR_out_temp_var,
                               font=Font(family='Helvetica', size=17, weight='bold'))
RR_out_temp_entry.grid(row=10, column=3, sticky='en', pady=10)

# RR_in_temp
RR_in_temp_label = tk.Label(root, text="Inner:")
RR_in_temp_label.grid(row=9, column=3, sticky='sw')

RR_in_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=RR_in_temp_var,
                              font=Font(family='Helvetica', size=17, weight='bold'))
RR_in_temp_entry.grid(row=10, column=3, sticky='nw', pady=10)

# RR_mid_temp
RR_mid_temp_label = tk.Label(root, text="Middle:")
RR_mid_temp_label.grid(row=9, column=3, sticky='s')

RR_mid_temp_entry = tk.Spinbox(root, from_=40, to=130, width=2, textvariable=RR_mid_temp_var,
                               font=Font(family='Helvetica', size=17, weight='bold'))
RR_mid_temp_entry.grid(row=10, column=3, sticky='n', pady=10)

# track_temp
track_temp_label = tk.Label(root, text="Track temp:")
track_temp_label.grid(row=5, column=1, sticky='e')

track_temp_entry = tk.Spinbox(root, from_=20, to=130, width=2, textvariable=track_temp_var,
                              font=Font(family='Helvetica', size=17, weight='bold'))
track_temp_entry.grid(row=5, column=2, sticky='w')

# brake_bias
brake_bias_label = tk.Label(root, text="Brake Bias:")
brake_bias_label.grid(row=4, column=1, sticky='se', pady=10)

brake_bias_entry = tk.Spinbox(root, from_=40, to=60, width=2, textvariable=brake_bias_var,
                              font=Font(family='Helvetica', size=17, weight='bold'))
brake_bias_entry.grid(row=4, column=2, sticky='sw', pady=10)
# FL Rebound Damper Setting
fl_rebound_label = tk.Label(root, text="FL Rebound Damper Setting:")
fl_rebound_label.grid(row=7, column=5, sticky='e')

fl_rebound_entry = tk.Spinbox(root, from_=1, to=12, width=2, textvariable=fl_rebound_var,
                              font=Font(family='Helvetica', size=17, weight='bold'))
fl_rebound_entry.grid(row=7, column=5, sticky='se')

# FL Compression Damper Setting
fl_compression_label = tk.Label(root, text="FL Compression Damper Setting:")
fl_compression_label.grid(row=8, column=5, sticky='en')

fl_compression_entry = tk.Spinbox(root, from_=1, to=12, width=2, textvariable=fl_compression_var,
                                  font=Font(family='Helvetica', size=17, weight='bold'))
fl_compression_entry.grid(row=8, column=5, sticky='se')

# FR Rebound Damper Setting
fr_rebound_label = tk.Label(root, text="FR Rebound Damper Setting:")
fr_rebound_label.grid(row=7, column=7, sticky='w')

fr_rebound_entry = tk.Spinbox(root, from_=1, to=12, width=2, textvariable=fr_rebound_var,
                              font=Font(family='Helvetica', size=17, weight='bold'))
fr_rebound_entry.grid(row=7, column=7, sticky='sw')

# FR Compression Damper Setting
fr_compression_label = tk.Label(root, text="FR Compression Damper Setting:")
fr_compression_label.grid(row=8, column=7, sticky='wn')

fr_compression_entry = tk.Spinbox(root, from_=1, to=12, width=2, textvariable=fr_compression_var,
                                  font=Font(family='Helvetica', size=17, weight='bold'))
fr_compression_entry.grid(row=8, column=7, sticky='sw')

# RL Rebound Damper Setting
rl_rebound_label = tk.Label(root, text="RL Rebound Damper Setting:")
rl_rebound_label.grid(row=9, column=5, sticky='e')

rl_rebound_entry = tk.Spinbox(root, from_=1, to=12, width=2, textvariable=rl_rebound_var,
                              font=Font(family='Helvetica', size=17, weight='bold'))
rl_rebound_entry.grid(row=9, column=5, sticky='se')

# RL Compression Damper Setting
rl_compression_label = tk.Label(root, text="RL Compression Damper Setting:")
rl_compression_label.grid(row=10, column=5, sticky='en')

rl_compression_entry = tk.Spinbox(root, from_=1, to=12, width=2, textvariable=rl_compression_var,
                                  font=Font(family='Helvetica', size=17, weight='bold'))
rl_compression_entry.grid(row=10, column=5, sticky='e')

# RR Rebound Damper Setting
rr_rebound_label = tk.Label(root, text="RR Rebound Damper Setting:")
rr_rebound_label.grid(row=9, column=7, sticky='w')

rr_rebound_entry = tk.Spinbox(root, from_=1, to=12, width=2, textvariable=rr_rebound_var,
                              font=Font(family='Helvetica', size=17, weight='bold'))
rr_rebound_entry.grid(row=9, column=7, sticky='sw')

# RR Compression Damper Setting
rr_compression_label = tk.Label(root, text="RR Compression Damper Setting:")
rr_compression_label.grid(row=10, column=7, sticky='wn')

rr_compression_entry = tk.Spinbox(root, from_=1, to=12, width=2, textvariable=rr_compression_var,
                                  font=Font(family='Helvetica', size=17, weight='bold'))
rr_compression_entry.grid(row=10, column=7, sticky='w')

# FW_angle
FW_angle_label = tk.Label(root, text="FW angle: ")
FW_angle_label.grid(row=3, column=5, sticky='e')

FW_angle_entry = tk.StringVar(root)
FW_angle_entry.set("option 1")  # Default value for the dropdown
FW_angle_dropdown = ttk.Combobox(root, textvariable=FW_angle_entry, width=17)
FW_angle_dropdown['values'] = ('Option 1', 'Option 2', 'Option 3')  # Set values for the dropdown
FW_angle_dropdown.grid(row=3, column=6, sticky='w')

# camber
camber_label = tk.Label(root, text="Camber: ")
camber_label.grid(row=2, column=5, sticky='e')

camber_entry = tk.StringVar(root)
camber_entry.set("option 1")  # Default value for the dropdown
camber_dropdown = ttk.Combobox(root, textvariable=camber_entry, width=17)
camber_dropdown['values'] = ('Option 1', 'Option 2', 'Option 3')  # Set values for the dropdown
camber_dropdown.grid(row=2, column=6, sticky='w')

# toe
toe_label = tk.Label(root, text="Toe: ")
toe_label.grid(row=1, column=5, sticky='e')

toe_entry = tk.StringVar(root)
toe_entry.set("option 1")  # Default value for the dropdown
toe_dropdown = ttk.Combobox(root, textvariable=toe_entry, width=17)
toe_dropdown['values'] = ('Option 1', 'Option 2', 'Option 3')  # Set values for the dropdown
toe_dropdown.grid(row=1, column=6, sticky='w')

# pedal_box_throttle_position
pedal_box_throttle_position_label = tk.Label(root, text="Pedal box throttle position: ")
pedal_box_throttle_position_label.grid(row=3, column=3, sticky='e')

pedal_box_throttle_position_entry = tk.StringVar(root)
pedal_box_throttle_position_entry.set("option 1")  # Default value for the dropdown
pedal_box_throttle_position_dropdown = ttk.Combobox(root, textvariable=pedal_box_throttle_position_entry, width=17)
pedal_box_throttle_position_dropdown['values'] = ('Option 1', 'Option 2', 'Option 3')  # Set values for the dropdown
pedal_box_throttle_position_dropdown.grid(row=3, column=4, sticky='w')

# pedal_box_brake_position
pedal_box_brake_position_label = tk.Label(root, text="Pedal box brake position: ")
pedal_box_brake_position_label.grid(row=2, column=3, sticky='e')

pedal_box_brake_position_entry = tk.StringVar(root)
pedal_box_brake_position_entry.set("option 1")  # Default value for the dropdown
pedal_box_brake_position_dropdown = ttk.Combobox(root, textvariable=pedal_box_brake_position_entry, width=17)
pedal_box_brake_position_dropdown['values'] = ('Option 1', 'Option 2', 'Option 3')  # Set values for the dropdown
pedal_box_brake_position_dropdown.grid(row=2, column=4, sticky='w')

# spring_rates
spring_rates_label = tk.Label(root, text="Spring rates: ")
spring_rates_label.grid(row=1, column=3, sticky='e')

spring_rates_entry = tk.StringVar(root)
spring_rates_entry.set("option 1")  # Default value for the dropdown
spring_rates_dropdown = ttk.Combobox(root, textvariable=spring_rates_entry, width=17)
spring_rates_dropdown['values'] = ('Option 1', 'Option 2', 'Option 3')  # Set values for the dropdown
spring_rates_dropdown.grid(row=1, column=4, sticky='w')

# ARB_setting
ARB_setting_label = tk.Label(root, text="ARB setting: ")
ARB_setting_label.grid(row=3, column=1, sticky='e')

ARB_setting_entry = tk.StringVar(root)
ARB_setting_entry.set("option 1")  # Default value for the dropdown
ARB_setting_dropdown = ttk.Combobox(root, textvariable=ARB_setting_entry)
ARB_setting_dropdown['values'] = ('Option 1', 'Option 2', 'Option 3')  # Set values for the dropdown
ARB_setting_dropdown.grid(row=3, column=2, sticky='w')

# differential_ramp_angle
differential_ramp_angle_label = tk.Label(root, text="Differential ramp angle: ")
differential_ramp_angle_label.grid(row=2, column=1, sticky='e')

differential_ramp_angle_entry = tk.StringVar(root)
differential_ramp_angle_entry.set("option 1")  # Default value for the dropdown
differential_ramp_angle_dropdown = ttk.Combobox(root, textvariable=differential_ramp_angle_entry)
differential_ramp_angle_dropdown['values'] = ('Option 1', 'Option 2', 'Option 3')  # Set values for the dropdown
differential_ramp_angle_dropdown.grid(row=2, column=2, sticky='w')

# R_wing_angle
R_wing_angle_label = tk.Label(root, text="Rear wing angle: ")
R_wing_angle_label.grid(row=1, column=1, sticky='e')

R_wing_angle_entry = tk.StringVar(root)
R_wing_angle_entry.set("option 1")  # Default value for the dropdown
R_wing_angle_dropdown = ttk.Combobox(root, textvariable=R_wing_angle_entry)
R_wing_angle_dropdown['values'] = ('Option 1', 'Option 2', 'Option 3')  # Set values for the dropdown
R_wing_angle_dropdown.grid(row=1, column=2, sticky='w')

# Button to save data
save_button = tk.Button(root, text="Save Data", command=save_data, bg="#86cf9a", height=2, width=15, )
save_button.grid(row=10, column=0, pady=10, sticky='')

select_label = tk.Label(root, text="View/Edit Outings:")
select_label.grid(row=9, column=0, pady=25)

# Dropdown to select data for editing
selected_entry = tk.StringVar(root)
selected_entry.set("Select Entry")  # Default value for the dropdown
selected_entry.trace("w", update_selected)  # Call update_selected when selected entry changes
dropdown = tk.OptionMenu(root, selected_entry, "Select Entry")
dropdown.grid(row=9, column=0, sticky='e', pady=15, padx=20)

# "New Outing" button
new_outing_button = tk.Button(root, text="New Outing", command=create_new_outing, bg="#CEB888", height=2, width=15, )
new_outing_button.grid(row=10, column=0, pady=5, sticky='e', padx=20)

# "Cancel" button
cancel_button = tk.Button(root, text="Cancel", command=cancel_update, bg="#cf8686", height=2, width=15, )
cancel_button.grid(row=10, column=0, sticky='e', padx=20)
cancel_button.grid_remove()

# Label to display editing message and time last saved
save_label = tk.Label(root, text="", fg="blue")
save_label.grid(row=9, column=0, sticky='s')

# Initial update of the dropdown menus
update_dropdown_options()

root.mainloop()