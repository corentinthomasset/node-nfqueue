{
  "targets": [
    {
      "target_name": "nfqueue",
      "sources": [
        "src/node_nfqueue.cpp"
      ],
      "libraries": [
        "-lnetfilter_queue"
      ],
      "cflags": [
        "-fpermissive"
      ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
