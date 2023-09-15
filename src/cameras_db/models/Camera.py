from math import sqrt
from typing import Optional


class Camera:
    """
    A camera
    """
    def __init__(
            self,
            brand: str,
            model: str,
            sensor_size_w: float,
            sensor_size_h: float,
            sensor_px_w: int,
            sensor_px_h: int,
            url: Optional[str] = None,
            image_url: Optional[str] = None,
            also_known_as: Optional[str] = None,
            year: Optional[int] = None,
            megapixels: Optional[float] = None,
            effective_megapixels: Optional[float] = None,
            total_megapixels: Optional[float] = None,
            sensor_size: Optional[str] = None,
            sensor_type: Optional[str] = None,
            sensor_resolution: Optional[str] = None,
            max_image_resolution: Optional[str] = None,
            crop_factor: Optional[float] = None,
            optical_zoom: Optional[float] = None,
            digital_zoom: Optional[int] = None,
            iso: Optional[str] = None,
            raw_support: Optional[int] = None,
            manual_focus: Optional[int] = None,
            normal_focus_range: Optional[str] = None,
            macro_focus_range: Optional[str] = None,
            focal_length_35mm_equiv: Optional[str] = None,
            aperture_priority: Optional[int] = None,
            max_aperture: Optional[str] = None,
            max_aperture_35mm_equiv: Optional[str] = None,
            depth_of_field: Optional[str] = None,
            metering: Optional[str] = None,
            exposure_compensation: Optional[str] = None,
            shutter_priority: Optional[int] = None,
            min_shutter_speed: Optional[str] = None,
            max_shutter_speed: Optional[str] = None,
            built_in_flash: Optional[int] = None,
            external_flash: Optional[int] = None,
            viewfinder: Optional[str] = None,
            white_balance_presets: Optional[int] = None,
            screen_size: Optional[str] = None,
            screen_resolution: Optional[str] = None,
            video_capture: Optional[int] = None,
            max_video_resolution: Optional[str] = None,
            storage_types: Optional[str] = None,
            usb: Optional[str] = None,
            hdmi: Optional[int] = None,
            wireless: Optional[int] = None,
            gps: Optional[str] = None,
            battery: Optional[str] = None,
            weight: Optional[float] = None,
            dimensions: Optional[str] = None,
    ) -> None:
        self.brand = brand
        self.model = model
        self.sensor_size_w = sensor_size_w
        self.sensor_size_h = sensor_size_h
        self.sensor_px_w = sensor_px_w
        self.sensor_px_h = sensor_px_h
        self.url = url
        self.image_url = image_url
        self.also_known_as = also_known_as
        self.year = year
        self.megapixels = megapixels
        self.effective_megapixels = effective_megapixels
        self.total_megapixels = total_megapixels
        self.sensor_size = sensor_size
        self.sensor_type = sensor_type
        self.sensor_resolution = sensor_resolution
        self.max_image_resolution = max_image_resolution
        self.crop_factor = crop_factor
        self.optical_zoom = optical_zoom
        self.digital_zoom = digital_zoom
        self.iso = iso
        self.raw_support = raw_support
        self.manual_focus = manual_focus
        self.normal_focus_range = normal_focus_range
        self.macro_focus_range = macro_focus_range
        self.focal_length_35mm_equiv = focal_length_35mm_equiv
        self.aperture_priority = aperture_priority
        self.max_aperture = max_aperture
        self.max_aperture_35mm_equiv = max_aperture_35mm_equiv
        self.depth_of_field = depth_of_field
        self.metering = metering
        self.exposure_compensation = exposure_compensation
        self.shutter_priority = shutter_priority
        self.min_shutter_speed = min_shutter_speed
        self.max_shutter_speed = max_shutter_speed
        self.built_in_flash = built_in_flash
        self.external_flash = external_flash
        self.viewfinder = viewfinder
        self.white_balance_presets = white_balance_presets
        self.screen_size = screen_size
        self.screen_resolution = screen_resolution
        self.video_capture = video_capture
        self.max_video_resolution = max_video_resolution
        self.storage_types = storage_types
        self.usb = usb
        self.hdmi = hdmi
        self.wireless = wireless
        self.gps = gps
        self.battery = battery
        self.weight = weight
        self.dimensions = dimensions

    def diagonal_size_mm(self) -> float:
        """Calculate the diagonal size of the sensor in millimeters."""
        return sqrt(self.sensor_size_w ** 2 + self.sensor_size_h ** 2)

    def diagonal_size_px(self) -> float:
        """Calculate the diagonal size of the sensor in pixels."""
        return sqrt(self.sensor_px_w ** 2 + self.sensor_px_h ** 2)

    @property
    def sensor(self) -> tuple:
        """Return a tuple containing the sensor attributes."""
        return self.sensor_size_w, self.sensor_size_h, self.sensor_px_w, self.sensor_px_h
