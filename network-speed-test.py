import speedtest
import subprocess
from time import sleep


st=speedtest.Speedtest()


def clear():
    subprocess.call('clear', shell=True)

def scan():
    clear()
    
    print("STARTING SCAN...")
    sleep(1)
    servernames = []
    
    print("FINDING FASTEST SERVER...")
    server = st.get_best_server(servernames)
    print(f"SERVER=[{server['host']}]")
    print(f"LATENCY=[{server['latency']}]")
    
    print("MEASURING DOWNLOAD SPEED...")
    download = float(st.download()/(1024*1024))
   
    print("MEASURING UPLOAD SPEED...")
    upload = float(st.upload()/(1024*1024))

    print("MEASURING PING...\n\n")
    ping = float(st.results.ping)


    subprocess.call('clear', shell=True)
    print("SERVER:    ", server['sponsor'])
    print("LOCATION:  ", server['name'])
    print("COUNTRY:   ", server['country'])
    print(f"LAT:        {server['lat']}")
    print(f"LON:        {server['lon']}\n")
    print("DOWNLOAD:  ", "%.2f" % download, "mbps")
    print("UPLOAD:    ", "%.2f" % upload, "mbps")
    print("PING:      ", "%.2f" % ping, "ms")



scan()
