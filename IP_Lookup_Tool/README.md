# IP Lookup Pro

**IP Lookup Pro** is a modern, avant-garde IP address analysis tool built with Python and CustomTkinter. It provides detailed geolocation data, ISP information, and interactive map visualization wrapped in a premium, ultra-responsive user interface.

## Features

- **Deep Analysis**: Get detailed info including ISP, City, Region, Zip Code, Timezone, and Coordinates.
- **Interactive Map**: Embedded map view to visualize the exact location of the IP/Domain.
- **Avant-Garde Design**: A sleek, modern UI with "Intentional Minimalism" design philosophy.
- **Premium Themes**: Switch between curated themes like Ocean Blue, Emerald, Rose Pink, Purple Rain, and Cyberpunk.
- **Multi-Language Support**: Full Turkish and English language support.
- **Clip & Go**: One-click copy functionality for all data fields.

## Installation / Run from Source

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/Memati8383/ip_tracer.git
    cd ip_tracer
    ```

2.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**:
    ```bash
    python main.py
    ```

## Build Executable (Windows)

To create a standalone `.exe` file:

```bash
pyinstaller --noconfirm --onefile --windowed --clean --icon=icon.ico --name "IPLookupPro" main.py
```

The executable will be located in the `dist/` folder.

## Technologies

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [TkinterMapView](https://github.com/TomSchimansky/TkinterMapView)
- Requests & IP-API
- Pillow (PIL)

## License

MIT License.
