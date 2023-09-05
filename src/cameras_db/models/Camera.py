# app/db/camera.py


class Camera:
    """
    Represents a camera.

    Attributes:
        sensor_size_w (float): The width of the camera sensor size.
        sensor_size_h (float): The height of the camera sensor size.
        sensor_px_w (int): The width of the camera sensor in pixels.
        sensor_px_h (int): The height of the camera sensor in pixels.
        url (str): The URL of the camera.
        image_url (str): The URL of the camera image.
        brand (str): The brand of the camera.
        model (str): The model of the camera.
        iso (list[str]): The supported ISO values of the camera.
        also_known_as (str): Other names or aliases for the camera.
        year (int): The year of the camera's release.
        max_aperture (str): The maximum aperture of the camera.
        crop_factor (str): The crop factor of the camera.
    """

    def __init__(
        self,
        sensor_size_w: float,
        sensor_size_h: float,
        sensor_px_w: int,
        sensor_px_h: int,
        url: str,
        image_url: str,
        brand: str,
        model: str,
        iso: [str],
        also_known_as: str,
        year: int,
        max_aperture: str,
        crop_factor: str,
    ) -> None:
        """
        Initializes a new Camera object.

        Args:
            sensor_size_w (float): The width of the camera sensor size.
            sensor_size_h (float): The height of the camera sensor size.
            sensor_px_w (int): The width of the camera sensor in pixels.
            sensor_px_h (int): The height of the camera sensor in pixels.
            url (str): The URL of the camera.
            image_url (str): The URL of the camera image.
            brand (str): The brand of the camera.
            model (str): The model of the camera.
            iso (list[str]): The supported ISO values of the camera.
            also_known_as (str): Other names or aliases for the camera.
            year (int): The year of the camera's release.
            max_aperture (str): The maximum aperture of the camera.
            crop_factor (str): The crop factor of the camera.
        """
        self.sensor_size_w = sensor_size_w
        self.sensor_size_h = sensor_size_h
        self.sensor_px_w = sensor_px_w
        self.sensor_px_h = sensor_px_h
        self.url = url
        self.image_url = image_url
        self.brand = brand
        self.model = model
        self.iso = iso
        self.also_known_as = also_known_as
        self.year = year
        self.max_aperture = max_aperture
        self.crop_factor = crop_factor
