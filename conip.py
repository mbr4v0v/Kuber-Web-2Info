from flask import Flask, request, render_template
import datetime
import socket

app = Flask(__name__)

@app.route("/")
def index():
  """Displays the current date, time, and the client's IP address."""

  now = datetime.datetime.now()
  current_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time

  # Get the client's IP address from the request headers.
  # request.remote_addr is often unreliable behind proxies or load balancers.
  # The common solution is to check for X-Forwarded-For (if your server sets it)
  client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

  hostname = socket.gethostname() # Get hostname
  host_ip = socket.gethostbyname(hostname) # Get the IP address of the host running the app

  return render_template("index.html", 
                         time=current_time, 
                         ip_address=client_ip,
                         hostname=hostname,
                         host_ip=host_ip)


if __name__ == "__main__":
  #  DO NOT USE debug=True IN PRODUCTION.  It's a security risk.
  app.run(debug=True, host='0.0.0.0')  # Listen on all interfaces (for accessibility)
