from speedtest import core

def print_speed(speed, unit):
  if unit == 'Mbps':
    if speed >= 50:
      color = 'green'
    elif speed >= 20:
      color = 'yellow'
    else:
      color = 'red'
  else:
    color = 'white'

  print(colored(f"{speed:.2f} {unit}", color))


def run_speed_test():
  print(colored("The connection speed test is starting...", "blue"))
  print()

  try:
    st = speedtest.core.Speedtest()
    st.get_best_server()

    print(colored("Download:", "cyan"))
    download_speed = st.download() / 10 ** 6 # Convert to Mbps
    print_speed(download_speed, 'Mbps')

    print(colored("\nUpload:", "cyan"))
    upload_speed = st.upload() / 10 ** 6 # Convert to Mbps
    print_speed(upload_speed, 'Mbps')

    print(colored("\nPing:", "cyan"))
    ping = st.results.ping
    print_speed(ping, 'ms')

    print()
    print(colored("The connection speed test is complete.\n", "green"))

  except speedtest.SpeedtestException:
    print(colored("An error occurred while performing the speed test\n", "red"))


if __name__ == "__main__":
  run_speed_test()
