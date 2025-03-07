# NBFC Fan Curve Plots

This repository is just for tinkering with fan configurations using **nbfc-linux**.

## Plots

Generated plots based on nbfc-linux JSON config files:

- Starting point 
  - **Acer Nitro AN515-43** 

    ![AN515-43](plots/Acer%20Nitro%20AN515-43.png)

  - **Acer Nitro AN515-57**

    ![AN515-57](plots/Acer%20Nitro%20AN515-57.png)

- **Acer Nitro AN515-45 Custom**

  ![AN515-45](plots/Acer%20Nitro%20AN515-45%20Custom.png)


## Configuration
Custom fan curve configurations are stored in the `settings/` folder.

- **Acer Nitro AN515-43:** `settings/Acer Nitro AN515-43.json`
- **Acer Nitro AN515-57:** `settings/Acer Nitro AN515-57.json`
- **Acer Nitro AN515-45 Custom:** `settings/Acer Nitro AN515-45 Custom.json`

## Usage

### To generate the plots

1. Install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Run the script:

    ```bash
    python plot.py
    ```

The generated plots will be saved in the `plots/` folder.

### To copy a configuration to the **nbfc-linux** config folder

```bash
./copy_settings.sh "Acer Nitro AN515-45 Custom.json"
```

