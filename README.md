# TailscaleUpDown

Program uses a mqtt switch controlled by Home Assistant to turn tailscale on or off (Up or Down).

Python is run in venv environment. To overcome externally managed Python and PIP conflicts.

```
cd /home/terry/TailscaleUpDown
source venv/bin/activate
python tailscale_mqtt.py
```

Copy any changes in the service to...

``` bash
sudo cp tgtailscale.service /etc/systemd/system/
```
then reload Systemd

``` bash
sudo systemctl restart tgtailscale.service
```
