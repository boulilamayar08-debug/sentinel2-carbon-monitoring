# sentinel-Carbon-Monitoring Pipeline

Satellite-based land monitoring pipeline for Alder Green Solutions,
built on Google Earth Engine. Tracks land cover and elevation over time
to support carbon credit measurement for sustainable farming in the
MENA region.

## Data sources
- **Sentinel-2 SR Harmonized** — optical imagery, 10m resolution, cloud-masked
- **ESA WorldCover v200** — land cover classification, 10m
- **SRTM (USGS)** — digital elevation model, ~30m, resampled to 10m
- **GEDI L4B** — biomass reference (pulled in Week 1; not usable for
  non-forest land, see Status below)

## Structure
