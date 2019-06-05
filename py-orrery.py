from skyfield.api import load, utc
from vpython import *
# import numpy as np
from datetime import datetime, timedelta

scene = canvas(title='PyOrrery',
               width=1000, height=1000  # ,
               # center=vector(5,0,0), background=color.cyan
               )  # This is needed in Jupyter notebook and lab to make programs easily rerunnable

G = 6.7e-11

planets = load('de421.bsp')  # ephemeris data from 1900 to 2053
sun, mercury, venus, earth, moon, mars = planets['sun'], planets['mercury'], planets['venus'], planets['earth'], planets['moon'], planets['mars']

jupiter, saturn, uranus, neptune, pluto = planets['jupiter_barycenter'], planets['saturn_barycenter'], planets['uranus_barycenter'], planets['neptune_barycenter'], planets['pluto_barycenter']

# real radii in AU
radius = {
    "sun": 0.00465040106951872,
    "mercury": 1.63034759358289E-05,
    "venus": 4.04545454545455E-05,
    "earth": 4.26336898395722E-05,
    "mars": 2.27072192513369E-05,
    "jupiter": 0.000477887700534759,
    "saturn": 0.000402860962566845,
    "uranus": 0.000170848930481283,
    "neptune": 0.000165548128342246,
    "pluto": 7.92112299465241E-06,
    "moon": 1.16116310160428E-05
}
inner_scale = 1000
outer_scale = 1000
# inner_scale = 1
# outer_scale = 1

ts = load.timescale()
time_step = timedelta(days=10)
dt = datetime(1900, 6, 1, tzinfo=utc)
t = ts.utc(dt)

sun_xyz = sun.at(t).observe(sun).cirs_xyz(ts.utc(dt + time_step)).au
sun_vec = vector(sun_xyz[0], sun_xyz[1], sun_xyz[2])

mercury_xyz = sun.at(t).observe(mercury).cirs_xyz(ts.utc(dt + time_step)).au
mercury_vec = vector(mercury_xyz[0], mercury_xyz[1], mercury_xyz[2])

venus_xyz = sun.at(t).observe(venus).cirs_xyz(ts.utc(dt + time_step)).au
venus_vec = vector(venus_xyz[0], venus_xyz[1], venus_xyz[2])

earth_xyz = sun.at(t).observe(earth).cirs_xyz(ts.utc(dt + time_step)).au
earth_vec = vector(earth_xyz[0], earth_xyz[1], earth_xyz[2])

# moon_xyz = sun.at(t).observe(moon).cirs_xyz(ts.utc(dt + time_step)).au
# moon_vec = vector(moon_xyz[0], moon_xyz[1], moon_xyz[2])

mars_xyz = sun.at(t).observe(mars).cirs_xyz(ts.utc(dt + time_step)).au
mars_vec = vector(mars_xyz[0], mars_xyz[1], mars_xyz[2])

jupiter_xyz = sun.at(t).observe(jupiter).cirs_xyz(ts.utc(dt + time_step)).au
jupiter_vec = vector(jupiter_xyz[0], jupiter_xyz[1], jupiter_xyz[2])

saturn_xyz = sun.at(t).observe(saturn).cirs_xyz(ts.utc(dt + time_step)).au
saturn_vec = vector(saturn_xyz[0], saturn_xyz[1], saturn_xyz[2])

uranus_xyz = sun.at(t).observe(uranus).cirs_xyz(ts.utc(dt + time_step)).au
uranus_vec = vector(uranus_xyz[0], uranus_xyz[1], uranus_xyz[2])

neptune_xyz = sun.at(t).observe(neptune).cirs_xyz(ts.utc(dt + time_step)).au
neptune_vec = vector(neptune_xyz[0], neptune_xyz[1], neptune_xyz[2])

pluto_xyz = sun.at(t).observe(pluto).cirs_xyz(ts.utc(dt + time_step)).au
pluto_vec = vector(pluto_xyz[0], pluto_xyz[1], pluto_xyz[2])

sun_sph = sphere(pos=sun_vec, radius=0.1, color=color.yellow)

mercury_sph = sphere(pos=mercury_vec, radius=inner_scale * radius['mercury'], color=color.orange, make_trail=True)

venus_sph = sphere(pos=venus_vec, radius=inner_scale * radius['venus'], color=color.white, make_trail=True)

earth_sph = sphere(pos=earth_vec, radius=inner_scale * radius['earth'], color=color.blue, make_trail=True)

# moon_sph = sphere(pos=moon_vec, radius=inner_scale * radius['moon'], color=color.white, make_trail=True)

mars_sph = sphere(pos=mars_vec, radius=inner_scale * radius['mars'], color=color.red, make_trail=True)

jupiter_sph = sphere(pos=jupiter_vec, radius=outer_scale * radius['jupiter'], color=color.orange, make_trail=True)

saturn_sph = sphere(pos=saturn_vec, radius=outer_scale * radius['saturn'], color=color.green, make_trail=True)

uranus_sph = sphere(pos=uranus_vec, radius=outer_scale * radius['uranus'], color=color.red, make_trail=True)

neptune_sph = sphere(pos=neptune_vec, radius=outer_scale * radius['neptune'], color=color.cyan, make_trail=True)

pluto_sph = sphere(pos=pluto_vec, radius=inner_scale * radius['pluto'], color=color.white, make_trail=True)


while True:
    rate(200)
    dt = dt + time_step
    new_t = ts.utc(dt)
    scene.title = dt.strftime("%b %Y")

    mercury_xyz = sun.at(new_t).observe(mercury).cirs_xyz(new_t).au
    mercury_sph.pos = vector(mercury_xyz[0], mercury_xyz[1], mercury_xyz[2])

    venus_xyz = sun.at(new_t).observe(venus).cirs_xyz(new_t).au
    venus_sph.pos = vector(venus_xyz[0], venus_xyz[1], venus_xyz[2])

    earth_xyz = sun.at(new_t).observe(earth).cirs_xyz(new_t).au
    earth_sph.pos = vector(earth_xyz[0], earth_xyz[1], earth_xyz[2])

    # moon_xyz = sun.at(new_t).observe(moon).cirs_xyz(new_t).au
    # moon_sph.pos = vector(moon_xyz[0], moon_xyz[1], moon_xyz[2])

    mars_xyz = sun.at(new_t).observe(mars).cirs_xyz(new_t).au
    mars_sph.pos = vector(mars_xyz[0], mars_xyz[1], mars_xyz[2])

    jupiter_xyz = sun.at(new_t).observe(jupiter).cirs_xyz(new_t).au
    jupiter_sph.pos = vector(jupiter_xyz[0], jupiter_xyz[1], jupiter_xyz[2])

    saturn_xyz = sun.at(new_t).observe(saturn).cirs_xyz(new_t).au
    saturn_sph.pos = vector(saturn_xyz[0], saturn_xyz[1], saturn_xyz[2])

    uranus_xyz = sun.at(new_t).observe(uranus).cirs_xyz(new_t).au
    uranus_sph.pos = vector(uranus_xyz[0], uranus_xyz[1], uranus_xyz[2])

    neptune_xyz = sun.at(new_t).observe(neptune).cirs_xyz(new_t).au
    neptune_sph.pos = vector(neptune_xyz[0], neptune_xyz[1], neptune_xyz[2])

    pluto_xyz = sun.at(new_t).observe(pluto).cirs_xyz(new_t).au
    pluto_sph.pos = vector(pluto_xyz[0], pluto_xyz[1], pluto_xyz[2])
