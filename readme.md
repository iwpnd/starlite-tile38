<br />
<p align="center">
  <h3 align="center">Starlite-Tile38</h3>

  <p align="center">
    Showcase using Tile38 via pyle38 in a Starlite application.
    <br />
    <a href="https://github.com/iwpnd/starlite-tile38/issues">Report Bug</a>
    ·
    <a href="https://github.com/iwpnd/starlite-tile38/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Showcase of using [Tile38](https://github.com/tidwall/tile38) with [Pyle38](https://github.com/iwpnd/pyle38) in a [Starlite](https://github.com/starlite-api/starlite)
application. Can be used as is, or be extended upon with other methods in the [pyle38 repertoire](https://github.com/iwpnd/pyle38#commands) of commands.

### Built With

-   [Starlite](https://github.com/starlite-api/starlite)
-   [Pyle38](https://github.com/iwpnd/pyle38)
-   [Tile38](https://github.com/tidwall/tile38)

<!-- GETTING STARTED -->

## Getting Started

### Installation

1. Clone and install
    ```sh
    git clone https://github.com/iwpnd/starlite-tile38.git
    poetry install
    ```
2. Setup environment
    ```sh
    TODO
    ```
3. Start your local stack
    ```python
    docker-compose up
    ```
4. Test it!
    ```sh
    pytest . -vv -s
    ```

## Usage

Once the application is started you can checkout and interact with it via on [localhost:8001/schema/redoc](http://localhost:8001/schema/redoc).

Or you can use it with [http](https://httpie.io/)/[curl](https://curl.se/):

```sh
echo '{ "data": { "type": "Feature", "geometry": {"type": "Point", "coordinates": [13.37, 52.25]}, "properties": {"id": "truck"}}}' \
      | http post http://localhost:8001/vehicles

> {data:"type":"Feature","geometry":{"type":"Point","coordinates":[13.37, 52.25]},"properties":{"id":"truck"}}


http get http://localhost:8001/vehicles/truck

> {data:"type":"Feature","geometry":{"type":"Point","coordinates":[13.37, 52.25]},"properties":{"id":"truck"}}

http get http://localhost:8001/vehicles

> { data: ["type":"Feature","geometry":{"type": "Point", "coordinates": [13.37, 52.25]},"properties":{"id":"truck"}]}
```

Or you use it with [httpx](https://www.python-httpx.org/)/[requests](https://docs.python-requests.org/en/master/):

```python
import httpx

vehicle = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [13.37, 52.25]},
    "properties": {"id": "truck"},
}

# store a vehicle
r = httpx.post(
      url="http://localhost:8001/vehicles",
      json={"data": vehicle}
      )

print(r.json())
> { data: ["type":"Feature","geometry":{"type": "Point", "coordinates": [13.37, 52.25]},"properties":{"id":"truck"}]}

# get a vehicle
r = httpx.get(
      url="http://localhost:8001/vehicles/truck",
      )

print(r.json())

> {"data": {"type":"Feature","geometry": {"coordinates": [13.37,52.25],"type": "Point"},"properties": {"id": "truck"}}}
```

You get the idea. And can use the rest.

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Benjamin Ramser - [@imwithpanda](https://twitter.com/imwithpanda) - ahoi@iwpnd.pw  
Project Link: [https://github.com/iwpnd/fastapi-tile38](https://github.com/iwpnd/fastapi-tile38)
