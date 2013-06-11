from django.conf.urls import patterns, url

from kitsune.forums.feeds import ThreadsFeed, PostsFeed


urlpatterns = patterns('kitsune.forums.views',
    url(r'^$', 'forums', name='forums.forums'),
    url(r'^/post-preview-async$', 'post_preview_async',
        name='forums.post_preview_async'),

    # TODO: Factor out `/(?P<forum_slug>\d+)` below
    url(r'^/(?P<forum_slug>[\w\-]+)$', 'threads', name='forums.threads'),
    url(r'^/(?P<forum_slug>[\w\-]+)/new$', 'new_thread',
        name='forums.new_thread'),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)$',
        'posts', name='forums.posts'),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)/reply$',
        'reply', name='forums.reply'),
    url(r'^/(?P<forum_slug>[\w\-]+)/feed$',
        ThreadsFeed(), name="forums.threads.feed"),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)/feed$',
        PostsFeed(), name="forums.posts.feed"),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)/lock$',
        'lock_thread', name='forums.lock_thread'),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)/sticky$',
        'sticky_thread', name='forums.sticky_thread'),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)/edit$',
        'edit_thread', name='forums.edit_thread'),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)/delete$',
        'delete_thread', name='forums.delete_thread'),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)/move$',
        'move_thread', name='forums.move_thread'),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)/(?P<post_id>\d+)/edit$',
        'edit_post', name='forums.edit_post'),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)/(?P<post_id>\d+)/delete$',
        'delete_post', name='forums.delete_post'),
    url(r'^/(?P<forum_slug>[\w\-]+)/(?P<thread_id>\d+)/watch',
        'watch_thread', name='forums.watch_thread'),
    url(r'^/(?P<forum_slug>[\w\-]+)/watch',
        'watch_forum', name='forums.watch_forum'),
)