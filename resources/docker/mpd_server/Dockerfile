FROM hypriot/rpi-alpine-scratch

RUN apk update && apk upgrade && apk add \
  bash \
  sudo \
  mpd \
  mpdscribble \
  alsa-utils

RUN mkdir -p /media/MEDIA/mpd/music \
    && mkdir -p /media/MEDIA/mpd/playlists \
    && touch /media/MEDIA/mpd/state \
    && touch /media/MEDIA/mpd/tag_cache \
    && chmod 777 -R /media/MEDIA/mpd \
    && chown -R mpd /media/MEDIA/mpd

COPY mpd.conf /etc/mpd.conf
COPY mpdscribble.conf /etc/mpdscribble.conf
COPY start.sh /start.sh

EXPOSE 8080 8000 6600

ENTRYPOINT ["/start.sh"]
