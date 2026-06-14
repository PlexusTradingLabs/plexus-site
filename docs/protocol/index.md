![](../assets/emblem-protocol.png){ .section-emblem }

# The Plexus Bus

The **Plexus Bus** is the protocol at the heart of everything — the nervous system that
carries information between every component instantly. It is the reason a strategy, a
monitor, and a trade client written in three different languages all speak as one.

!!! note "Read the full spec"
    The complete wire spec — message types, transports, the security seam, encoding
    negotiation, and the golden conformance vectors — lives in the **plexus-protocol**
    repository and its wiki, right next to the harness that keeps all three implementations
    in parity.

    [:material-book-open-variant: Protocol wiki](https://github.com/PlexusTradingLabs/plexus-protocol/wiki){ .md-button } &nbsp;
    [:fontawesome-brands-github: plexus-protocol repo](https://github.com/PlexusTradingLabs/plexus-protocol){ .md-button }

## Three implementations, one protocol

The same wire protocol is implemented independently in three languages and kept in
lockstep by a conformance harness that tests the **published packages**, not co-located
source:

| Implementation | Package | Registry |
|---|---|---|
| Rust | `plexus-bus` | crates.io |
| Python | `plexus_bus` | PyPI |
| .NET | `Plexus.Bus` | NuGet |

## The plugin handshake

A Python plugin never touches a socket. It registers handlers with the Rust host; the bus
mechanics — dispatch, reply, security, metrics — are all handled for you.

```mermaid
sequenceDiagram
  participant Bus as Plexus Bus
  participant Host as PrismR host (Rust)
  participant Plug as Your Python plugin
  Note over Host,Plug: on_load(host) registers your RPCs
  Bus->>Host: RPC "forecast" {closes, horizon}
  Host->>Plug: fn(payload)
  Plug->>Host: host.cache_get / cache_put
  Plug-->>Host: forecast cone (p10/p50/p90)
  Host-->>Bus: reply
```

[Write a plugin :octicons-arrow-right-24:](../prismr/plugins.md){ .md-button }
