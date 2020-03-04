<h1 align="center"><img src="http://icons.iconarchive.com/icons/ncrow/mega-pack-2/256/AOL-icon.png" width="50" alt="aol" /> AOLoL</h1>

<p align="center">
  <strong>cOnNecTiOn aNiMaTiOn f0r LiNuX, i3 oR wHaTeVeR</strong>
</p>

<p align="center">
  <em>Connect to the internet free for 30-days!</em>
</p>

[![screenshot](https://user-images.githubusercontent.com/132562/75916852-e9e66e00-5e0d-11ea-990b-09f4ec56c3ce.gif)](https://user-images.githubusercontent.com/132562/75916861-ec48c800-5e0d-11ea-809e-02ccf8644679.gif)


## Requirements

- `scrot`
- `convert`
- i3 ?
    - `i3lock`
- no i3 ?
    - python
    - `pip install pygame`

## Setup

```sh
mkdir -p /usr/share/aolol
cp aol-frame* /usr/share/aolol
```

then copy either [aolol.sh](./aolol.sh) __for i3__
or [aolol.py](./aolol.py) to somewhere in your path, like `~/.local/bin`

## i3 Config Example

example showing animation during vpn connect
use either `python ~/.local/bin/aolol.py;` or `~/.local/bin/aolol.sh;`

```
set $mode_vpn VPN (v) enable, (V) disable, (r)estart
mode "$mode_vpn" {
    bindsym v exec --no-startup-id "python ~/.local/bin/aolol.py; sudo systemctl start openvpn", mode "default"
    bindsym Shift+v exec --no-startup-id sudo systemctl stop openvpn, mode "default"
    bindsym r exec --no-startup-id sudo systemctl restart openvpn, mode "default"

    bindsym Return mode "default"
    bindsym Escape mode "default"
}
bindsym $mod+v mode "$mode_vpn"
```
