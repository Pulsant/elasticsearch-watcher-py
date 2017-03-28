from elasticsearch.client.utils import (AddonClient,
                                        query_params,
                                        _make_path,
                                        SKIP_IN_PATH)


class WatcherClient(AddonClient):
    namespace = 'watcher'

    @query_params()
    def info(self, params=None):
        """
        Get info about the xpack plugin.
        `<https://www.elastic.co/guide/en/x-pack/current/info-api.html>`_
        """
        data = self.transport.perform_request('GET',
                                              _make_path('_xpack'),
                                              params=params)
        return data

    @query_params('master_timeout')
    def put_watch(self, watch_id, body, params=None):
        """
        Create a watcher.
        `<https://www.elastic.co/guide/en/x-pack/current/watcher-api-put-watch.html>`_

        :arg watch_id: Watch ID
        :arg body: The watch
        :arg master_timeout: Specify timeout for watch write operation
        """
        for param in (watch_id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        data = self.transport.perform_request('PUT',
                                              _make_path('_xpack',
                                                         'watcher',
                                                         'watch',
                                                         watch_id),
                                              params=params, body=body)
        return data

    @query_params()
    def stats(self, params=None):
        """
        Get stats for the watcher plugin.
        `<https://www.elastic.co/guide/en/x-pack/current/watcher-api-stats.html>`_
        """

        data = self.transport.perform_request('GET',
                                              _make_path('_xpack',
                                                         'watcher',
                                                         'stats'),
                                              params=params)
        return data

    @query_params()
    def stop(self, params=None):
        """
        Stop the watcher service.
        `<https://www.elastic.co/guide/en/x-pack/current/watcher-api-stop.html>`_
        """

        data = self.transport.perform_request('PUT',
                                              _make_path('_xpack',
                                                         '_watcher',
                                                         '_stop'),
                                              params=params)
        return data

    @query_params()
    def start(self, params=None):
        """
        Start the watcher service.
        `<https://www.elastic.co/guide/en/x-pack/current/watcher-api-start.html>`_
        """

        data = self.transport.perform_request('PUT',
                                              _make_path('_xpack',
                                                         'watcher',
                                                         '_start'),
                                              params=params)
        return data

    @query_params('master_timeout')
    def ack_watch(self, watch_id, params=None):
        """
        Ack a watch.
        `<https://www.elastic.co/guide/en/x-pack/current/watcher-api-ack-watch.html>`_

        :arg watch_id: Watch ID
        :arg master_timeout: Specify timeout for watch write operation
        """

        if watch_id in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'watch_id'.")

        data = self.transport.perform_request('PUT',
                                              _make_path('_xpack',
                                                         'watcher',
                                                         'watch',
                                                         watch_id,
                                                         '_ack'),
                                              params=params)
        return data

    @query_params()
    def execute_watch(self, watch_id, body=None, params=None):
        """
        Execute watch manually.
        `<https://www.elastic.co/guide/en/x-pack/current/watcher-api-execute-watch.html>`_

        :arg watch_id: Watch ID
        :arg body: Execution control
        """

        if watch_id in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'watch_id'.")

        data = self.transport.perform_request('POST',
                                              _make_path('_xpack',
                                                         'watcher',
                                                         'watch',
                                                         watch_id,
                                                         '_execute'),
                                              params=params,
                                              body=body)
        return data

    @query_params()
    def get_watch(self, watch_id, params=None):
        """
        Retrieve watch definition.
        `<https://www.elastic.co/guide/en/x-pack/current/watcher-api-get-watch.html>`_

        :arg watch_id: Watch ID
        """
        if watch_id in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'watch_id'.")

        data = self.transport.perform_request('GET',
                                              _make_path('_xpack',
                                                         'watcher',
                                                         'watch',
                                                         watch_id),
                                              params=params)
        return data

    @query_params('force', 'master_timeout')
    def delete_watch(self, watch_id, params=None):
        """
        Delete a watch.
        `<https://www.elastic.co/guide/en/x-pack/current/watcher-api-delete-watch.html>`_

        :arg watch_id: Watch ID
        :arg force: Specify if this request should be forced and ignore locks
        :arg master_timeout: Specify timeout for watch write operation
        """
        if watch_id in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'watch_id'.")

        data = self.transport.perform_request('DELETE',
                                              _make_path('_xpack',
                                                         'watcher',
                                                         'watch',
                                                         watch_id),
                                              params=params)

        return data

    @query_params()
    def restart(self, params=None):
        """
        Restart the watcher service.
        `<https://www.elastic.co/guide/en/x-pack/current/watcher-api-restart.html>`_
        """

        data = self.transport.perform_request('POST',
                                              _make_path('_xpack',
                                                         'watcher',
                                                         '_restart'),
                                              params=params)
        return data
