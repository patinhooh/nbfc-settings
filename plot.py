import os
import json
import matplotlib.pyplot as plt


def plot_fan_curve(data, filename):
    fan_configs = data.get("FanConfigurations", [])
    colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F']  # Just some nice RGB colors

    for index, fan in enumerate(fan_configs):
        fan_name = fan["FanDisplayName"]
        thresholds = fan["TemperatureThresholds"]

        up_temps = [t["UpThreshold"] for t in thresholds]
        down_temps = [t["DownThreshold"] for t in thresholds]
        speeds = [t["FanSpeed"] for t in thresholds]

        plt.plot(up_temps, speeds, label=f"{fan_name} (UpThreshold)", color=colors[index % len(colors)], linewidth=1.5)
        plt.plot(down_temps, speeds, linestyle='dashed', label=f"{fan_name} (DownThreshold)", color=colors[index % len(colors)], linewidth=1)

    plt.title(f"Fan Curve: {filename}")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Fan Speed (%)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Save image as PNG
    image_filename = filename.replace(".json", ".png")
    plt.savefig(image_filename)
    print(f"Image saved: {image_filename}")
    plt.close()


def main():
    folder = os.path.dirname(__file__)
    files = [f for f in os.listdir(folder) if f.endswith(".json")]

    if not files:
        print("No JSON files found.")
        return

    for file in files:
        try:
            with open(file, "r") as json_file:
                data = json.load(json_file)
                plot_fan_curve(data, file)
        except Exception as e:
            print(f"Failed to process {file}: {e}")


if __name__ == "__main__":
    main()