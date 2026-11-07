# models.py

class Title:
    def __init__(self, title_id: int, name: str, release_year: int):
        self.title_id = title_id
        self.name = name
        self.release_year = release_year

class Season:
    def __init__(self, season_id: int, title_id: int, season_number: int):
        self.season_id = season_id
        self.title_id = title_id
        self.season_number = season_number

class Episode:
    def __init__(self, episode_id: int, season_id: int, episode_title: str, duration_seconds: int):
        self.episode_id = episode_id
        self.season_id = season_id
        self.episode_title = episode_title
        self.duration_seconds = duration_seconds

class Review:
    def __init__(self, review_id: int, title_id: int, rating_stars: int, review_text: str):
        self.review_id = review_id
        self.title_id = title_id
        self.review_text = review_text
        self.review_text = review_text