# Code to get a new identity from tor

To use this code it is required that the tor control port is on

Make the following changes in the torrc file:
1. Enable the control port by uncommenting:
  `ControlPort 9051` 
from /etc/tor/torrc
2. Set the empty password, otherwise it gives `515 Authentication failed: Wrong length on authentication cookie.`. First run:
  `tor --hash-password <password>`
This outputs something like:
`16:D14CC89AD7848B8C60093105E8284A2D3AB2CF3C20D95FECA0848CFAD2`
Now on `/etc/tor/torrc` update the line:
`HashedControlPassword 16:D14CC89AD7848B8C60093105E8284A2D3AB2CF3C20D95FECA0848CFAD2`
3. Restart tor.
